from django.db import models
from materia.models import Materia

# Create your models here.

class Turma(models.Model):
    turma = models.CharField(max_length=50)
    materias = models.ManyToManyField(Materia)

    def __str__(self):
        return self.turma