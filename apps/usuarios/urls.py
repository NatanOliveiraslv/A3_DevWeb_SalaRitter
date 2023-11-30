from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'clients'

router = routers.DefaultRouter()
router.register('professor', views.ProfessorViewSet, basename='professor')
router.register('aluno', views.AlunoViewSet, basename='aluno')

urlpatterns = [
    path('', include(router.urls) )
]
