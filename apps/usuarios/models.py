from django.db import models
from django.contrib.auth.models import User


class Professor(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome

from turma.models import Turma

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome