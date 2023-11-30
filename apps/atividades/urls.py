from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'atividade'

router = routers.DefaultRouter()
router.register('atividade', views.AtividadeViewSet, basename='atividade')
router.register('atividadeConcluida', views.AtividadeConcluidaViewSet, basename='atividadeConcluida')

urlpatterns = [
    path('', include(router.urls) )
]