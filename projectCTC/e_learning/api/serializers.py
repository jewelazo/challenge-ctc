from rest_framework import serializers
from e_learning.models import Padre,Estudiante


class PadreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Padre
        fields="__all__"


class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Estudiante
        fields="__all__"