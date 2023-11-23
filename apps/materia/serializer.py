from .models import Materia
from rest_framework import serializers

class materiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = '__all__'
        
        # Para chamar todos os atributos:
        # fields = '__all__'
        
        # Para chamar somentes os atributos de interesse:
        # fields = ['id','created_on', 'updated_on', 'name', 'description']
