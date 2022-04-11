from rest_framework import serializers
from e_learning.models import Padre, Estudiante


class PadreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Padre
        exclude = ("creado", "editado")
        # fields="__all__"


class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        exclude = ("creado", "editado")
        # fields="__all__"
