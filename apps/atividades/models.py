from django.db import models
from materia.models import Materia
from usuarios.models import Aluno
from turma.models import Turma

class Atividade(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, null=True)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.titulo

class AtividadeConcluida(models.Model):
    resposta = models.TextField()
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE, null=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.resposta