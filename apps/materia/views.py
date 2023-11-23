from django.shortcuts import render
from .models import Materia
from rest_framework import viewsets
from .serializer import materiaSerializer

# Create your views here.

class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class =  materiaSerializer