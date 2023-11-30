from .models import Atividade, AtividadeConcluida
from rest_framework import viewsets
from .serializer import AtividadeSerializer, AtividadeConcluidaSerializer

# Após o comentario "# Create your views here." e crie as views "Category".

class AtividadeViewSet(viewsets.ModelViewSet):
    queryset = Atividade.objects.all()
    serializer_class = AtividadeSerializer  

class AtividadeConcluidaViewSet(viewsets.ModelViewSet):
    queryset = AtividadeConcluida.objects.all()
    serializer_class = AtividadeConcluidaSerializer