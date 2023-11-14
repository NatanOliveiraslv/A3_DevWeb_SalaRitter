from django.db import models
from django.contrib.auth.models import User

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)