from .models import Atividade, AtividadeConcluida
from rest_framework import serializers

class AtividadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atividade
        fields = '__all__'
class AtividadeConcluidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtividadeConcluida
        fields = '__all__'