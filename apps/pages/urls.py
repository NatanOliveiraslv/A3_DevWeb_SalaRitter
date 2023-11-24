from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('painel/', views.painelUsuario, name='painel'),
    #para o funcionamento desta Path, é necessário passar o id da turma
    path('painel/turma/<int:turma_id>', views.painelTurmas , name='painelTurmas'),
    path('painel/turma/alunos/<int:turma_id>', views.painelTurmasListaAlunos , name='listaAlunos'),
    path('painel/turma/cadastar_atividades/<int:turma_id>', views.painelTurmasCadastraAtividade , name='CadastraAtividade'),
]