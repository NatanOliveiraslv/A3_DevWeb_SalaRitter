from django.shortcuts import render
from .models import Turma
from rest_framework import viewsets
from .serializer import turmaSerializer

class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = turmaSerializer
