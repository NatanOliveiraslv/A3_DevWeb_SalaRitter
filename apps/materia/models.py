from django.db import models
from turma.models import Turma
from usuarios.models import Professor

# Create your models here.

class Materia(models.Model):
    materia = models.CharField(max_length=50)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, null=True)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.materia