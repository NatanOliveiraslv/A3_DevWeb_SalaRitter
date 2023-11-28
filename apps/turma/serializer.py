from .models import Turma
from rest_framework import serializers

class turmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'
