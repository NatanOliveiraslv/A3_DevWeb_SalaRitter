from django.shortcuts import redirect, render
from usuarios.models import Aluno, Professor
from materia.models import Materia
from turma.models import Turma
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import get_object_or_404

#Funçao para validar se o usuário está vinculado ao model Professor
def validaProfessor(usuario):
    try:
        Professor.objects.get(user=User.objects.get(username=usuario))
        return True
    except:
        return False
    
#Funçao para validar se o usuário está vinculado ao model Aluno 
def validaAluno(usuario):
    try:
        Aluno.objects.get(user=User.objects.get(username=usuario))
        return True
    except:
        return False

def index(request):

    #Se a requsiçao passada for post
    if request.method == "POST":
        usuario = request.POST.get("usuario")
        senha = request.POST.get("senha")
        #Com os dados passados, verifcar se é possível autenticar o usuário
        user = authenticate(username=usuario, password=senha)
        if user is not None:
            login(request, user) #loga o usuário
            return redirect('painel') # redireciona para o link /painel
        else:
            messages.error(request, 'Usuário ou senha incorreto!') 
            return redirect('index')
    else:
        return render(request, 'usuarios/login.html')

def painelUsuario(request):
    # se o usuário estiver logado
    if request.user.is_authenticated:
        # Acessar informações do usuário
        usuario = request.user.username
        #verifca se o usuário passado realmente é professor, ou se está vinculado a um professor
        if validaProfessor(usuario):
            # Obtém o professor associado ao usuário autenticado
            professor_autenticado = get_object_or_404(Professor, user=request.user)
            # Obtém todas as turmas onde o professor é o mesmo que o associado à matéria
            turma = Turma.objects.filter(materias__professor = professor_autenticado).distinct()

            return render(request, 'usuarios/painel_professor.html', {'turma':turma})
        elif validaAluno(usuario):
            return render(request, 'usuarios/painel_aluno.html')
        else:
            messages.error(request, 'Usuário não encotrado, ou nao está vinculado!')
            return redirect('index')
    else:
        messages.error(request, 'Usuário não autenticado. Faça o login para acessar a pagina desejada.')
        return redirect('index')

def painelTurmas(request, turma_id):
    return render(request, 'usuarios/painel_turmas_professor.html', {''})
