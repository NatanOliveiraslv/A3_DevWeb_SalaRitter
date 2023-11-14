from django.shortcuts import render
from pages.models import Aluno, Professor
from django.contrib.auth.models import User

def validaProfessor():
    try:
        Professor.objects.get(user=User.objects.get(username="professor"))
        return True
    except:
        return False
        
def validaAluno():
    try:
        Aluno.objects.get(user=User.objects.get(username="professor"))
        return True
    except:
        return False
    

# Create your views here.
def index(request):
    if validaProfessor():
        return render(request, 'usuarios/painel_professor.html')
    elif validaAluno():
        return render(request, 'usuarios/painel_aluno.html')
    else:
        return render(request, 'usuarios/login.html')