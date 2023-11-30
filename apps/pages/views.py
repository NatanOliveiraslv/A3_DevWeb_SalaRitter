from multiprocessing import context
import re
from django.shortcuts import redirect, render
from usuarios.models import Aluno, Professor
from materia.models import Materia
from turma.models import Turma
from atividades.models import Atividade, AtividadeConcluida
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
            #se nao atenticar, é porque o ussuário ou senha está erradp
            messages.error(request, 'Usuário ou senha incorreto!') 
            return redirect('index')
    else:
        # Se arequisição nao for post
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
            turma = Turma.objects.filter(materias__professor = professor_autenticado).distinct() #Está funçao distinct() serve para que nao seja inserdo n variavel turmas iguais
            return render(request, 'usuarios/professor/painel_professor.html', {'turma':turma})     
        elif validaAluno(usuario):
            # Se for aluno, envia para o painel do aluno
            aluno_autenticado = get_object_or_404(Aluno, user=request.user).turma
            materia = aluno_autenticado.materias.all()
            return render(request, 'usuarios/aluno/painel_aluno.html', {'materia':materia,
                                                                        'turma':aluno_autenticado})
        else:
            # Este erro iá ocorre se o usuário nao estiver vinculado a nenhum professor ou aluno
            messages.error(request, 'Usuário não encotrado, ou nao está vinculado!')
            return redirect('index')
    else:
        messages.error(request, 'Usuário não autenticado. Faça o login para acessar a pagina desejada.')
        return redirect('index')
        
def painelTurmas(request, turma_id):
    # se o usuário estiver logado
    if request.user.is_authenticated:
        # Acessar informações do usuário
        usuario = request.user.username
        #verifca se o usuário passado realmente é professor, ou se está vinculado a um professor
        if validaProfessor(usuario):
            #da requisção passado captura o id da turma
            turma = get_object_or_404(Turma, pk=turma_id) #atribui a variavel a turma com o id passado
            return render(request, 'usuarios/professor/tela_controle_professor.html', {'turma':turma})
        else:
            messages.error(request, 'Usuário nao atorizado à acessar a pagina.')
            return redirect('index')
    else:
        messages.error(request, 'Usuário não autenticado. Faça o login para acessar a pagina desejada.')
        return redirect('index')

def painelTurmasListaAlunos(request, turma_id):
    # se o usuário estiver logado
    if request.user.is_authenticated:
        # Acessar informações do usuário
        usuario = request.user.username
        #verifca se o usuário passado realmente é professor, ou se está vinculado a um professor
        if validaProfessor(usuario):
            #da requisção passado captura o id da turma
            turma = get_object_or_404(Turma, pk=turma_id) #atribui a variavel a turma com o id passado
            aluno = Aluno.objects.all().filter(turma=turma) #atribui a variavel todos os alunos da turma
            return render(request, 'usuarios/professor/tela_controle_professor_lista_alunos.html', {'turma':turma,
                                                                                                    'aluno':aluno})
        else:
            messages.error(request, 'Usuário nao atorizado à acessar a pagina.')
            return redirect('index')
    else:
        messages.error(request, 'Usuário não autenticado. Faça o login para acessar a pagina desejada.')
        return redirect('index')

def painelTurmasCadastraAtividade(request, turma_id):
    # se o usuário estiver logado
    if request.user.is_authenticated:
            # Acessar informações do usuário
            usuario = request.user.username
            #verifca se o usuário passado realmente é professor, ou se está vinculado a um professor
            if validaProfessor(usuario):
                turma = get_object_or_404(Turma, pk=turma_id) #atribui a variavel a turma com o id passado
                #se a requisiçao for POST         
                if request.method == 'POST':
                    #obtem os dados passado pelo professor
                    titulo = request.POST.get("titulo")
                    descricao = request.POST.get("descricao")
                    professor_autenticado = Professor.objects.get(user=User.objects.get(username=usuario)) #atribui a varaivel o professor autenticado
                    materia = Materia.objects.get(professor = professor_autenticado) #atribui a varaivel a materia do profeesor autenticado
                    # cria uma nova atividade
                    nova_atividade = Atividade.objects.create(
                        titulo=titulo,
                        descricao=descricao,
                        materia=materia,
                        turma=turma,
                    )

                    nova_atividade.save()
                    messages.success(request, 'Atividade cadastrada com sucesso!') 
                    return redirect('CadastraAtividade', turma_id)
                else:
                    return render(request, 'usuarios/professor/tela_controle_professor_cadatra_atividade.html', {'turma':turma})
            else:
                messages.error(request, 'Usuário nao atorizado à acessar a pagina.')
                return redirect('index')
    else:
        messages.error(request, 'Usuário não autenticado. Faça o login para acessar a pagina desejada.')
        return redirect('index')

def painelAlunoMateriaSelecao(request, materia_id):
     # se o usuário estiver logado
    if request.user.is_authenticated:
            # Acessar informações do usuário
            usuario = request.user.username
            #verifca se o usuário passado realmente é aluno, ou se está vinculado a um aluno
            if validaAluno(usuario):
                
                aluno_autenticado = get_object_or_404(Aluno, user=request.user) #atribui a varaivel o aluno autenticado
                aluno_autenticado_turma = aluno_autenticado.turma #atribui a varaivel a turma do aluno autenticado
                materia = aluno_autenticado_turma.materias.all() #atribui a variavel todas as meterias da turma do aluno
                atividades = Atividade.objects.filter(materia__id=materia_id, turma=aluno_autenticado_turma) #atribui a variavel todas as atividades da materia e da turma

                dados_atividades = [] # variavel array, criada para que seja passado os dados para a pagina, no formato configurado

                # Iterar sobre as atividades
                for atividade in atividades:
                    # Tentar recuperar a atividade concluída associada
                    try:
                        atividade_concluida = AtividadeConcluida.objects.get(atividade=atividade, aluno=aluno_autenticado)
                        status = 'Entregue'
                    except AtividadeConcluida.DoesNotExist:
                        atividade_concluida = None
                        status = 'Pendente'
                    # Passa os dados, para a variavel dados_atividades
                    dados_atividades.append({
                        'titulo': atividade.titulo,
                        'descricao': atividade.descricao,
                        'id': atividade.id,
                        'status': status,
                        'resposta': atividade_concluida.resposta if atividade_concluida else None,
                    })

                if request.method == 'POST':
                    resposta = request.POST.get("resposta") # Atribui a variavel a resposta passada
                    atividade_resposta = get_object_or_404(Atividade, pk=request.POST.get("id"))# Atribui a variavel a Atividade, conforme o ID da atividfade passado na request
                    
                    #if para validar se o aluno já entregou a atividades, e se caso entregue, apenas redireciona ele para mesma pagina
                    if(AtividadeConcluida.objects.all().filter(atividade = atividade_resposta, aluno = aluno_autenticado).first() is not None):
                        messages.error(request, 'Esta atividade já foi respondida')
                        print(AtividadeConcluida.objects.filter(atividade = atividade_resposta, aluno = aluno_autenticado) )
                        return redirect('materiaAtividades', materia_id)
                    
                    #Caso nao tenha sido entregue a atividade, cria uma nova atividade conculida.
                    else:
                        atividade_concluida = AtividadeConcluida.objects.create(
                            resposta=resposta,
                            atividade=atividade_resposta,
                            aluno=aluno_autenticado,
                        )
                        atividade_concluida.save()

                        messages.success(request, 'Resposta enviada com sucesso!')
                        return redirect('materiaAtividades', materia_id)
        
                #Se nao for Post a request
                else:
                    return render(request, 'usuarios/aluno/painel_aluno_materia_selecao.html', {'turma':aluno_autenticado_turma,
                                                                                                'materia':materia,
                                                                                                'atividade':dados_atividades})
            else:
                messages.error(request, 'Usuário nao atorizado à acessar a pagina.')
                return redirect('index')
    else:
        messages.error(request, 'Usuário não autenticado. Faça o login para acessar a pagina desejada.')
        return redirect('index')

def PainelTurmasAtividadesConcluidas(request,turma_id):
    # se o usuário estiver logado
    if request.user.is_authenticated:
            # Acessar informações do usuário
            usuario = request.user.username
            #verifca se o usuário passado realmente é aluno, ou se está vinculado a um aluno
            if validaProfessor(usuario):
                #da requisção passado captura o id da turma
                turma = get_object_or_404(Turma, pk=turma_id) #atribui a variavel a turma com o id passado
                professor_autenticado = get_object_or_404(Professor, user=request.user) #atribui a variavel o professor que está autenticado
                materia_professor = Materia.objects.get(professor=professor_autenticado) #atribui as materia que tem o professor
                atividade_professor = Atividade.objects.all().filter(materia=materia_professor, turma=turma) #atribui as atividades que sao da mesma materia do professor e da turma
                atividade_conluida = AtividadeConcluida.objects.all() # obtem todas as atividades conculidas

                return render(request, 'usuarios/professor/tela_controle_professor_atividades_concluidas.html', {'atividade': atividade_professor,
                                                                                                                 'atividade_conluida': atividade_conluida,
                                                                                                                 'turma': turma})
            else:
                messages.error(request, 'Usuário nao atorizado à acessar a pagina.')
                return redirect('index')
    else:
            messages.error(request, 'Usuário não autenticado. Faça o login para acessar a pagina desejada.')
            return redirect('index')
