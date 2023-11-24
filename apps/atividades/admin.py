from re import A
from django.contrib import admin
from .models import Atividade, AtividadeConcluida

admin.site.register(Atividade)
admin.site.register(AtividadeConcluida)