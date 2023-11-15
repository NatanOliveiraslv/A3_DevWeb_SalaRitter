from django.db import models

# Create your models here.

class Turma(models.Model):
    turma = models.CharField(max_length=50)

    def __str__(self):
        return self.turma