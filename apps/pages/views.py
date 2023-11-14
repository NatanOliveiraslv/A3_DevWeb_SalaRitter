from django.shortcuts import redirect, render
from usuarios.models import Aluno, Professor
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

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
            return render(request, 'usuarios/login.html')
    else:
        return render(request, 'usuarios/login.html')

def painelUsuario(request):
    # se o usuário estiver logado
    if request.user.is_authenticated:
        # Acessar informações do usuário
        usuario = request.user.username
        #verifca para qual pagina o usuário irá ser enviado. Se for aluno para a do aluno
        # se professor para a dor professor.
        if validaProfessor(usuario):
            return render(request, 'usuarios/painel_professor.html')
        elif validaAluno(usuario):
            return render(request, 'usuarios/painel_aluno.html')
        else:
            return HttpResponse("Usuario nao encotrado, ou nao está vinculado!")
    else:
        return HttpResponse("Usuário não autenticado. Faça o login para acessar esta página.")