from django.urls import path, include 
from . import views
from rest_framework import routers

app_name = 'turma'
router = routers.DefaultRouter()
router.register('turma', views.TurmaViewSet, basename='turma')

urlpatterns = [
    path('', include(router.urls))
]