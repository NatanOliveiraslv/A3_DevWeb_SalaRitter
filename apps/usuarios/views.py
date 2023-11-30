from .models import Professor, Aluno
from rest_framework import viewsets
from .serializer import ProfessorSerializer, AlunoSerializer

# Após o comentario "# Create your views here." e crie as views "Client".

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer  

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer