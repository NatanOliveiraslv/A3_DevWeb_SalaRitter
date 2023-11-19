from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('painel/', views.painelUsuario, name='painel'),
    path('painel/turma/<int:turma_id>', views.painelTurmas , name='painelTurmas')
]