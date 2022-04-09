from rest_framework import serializers
from e_learning.models import Padre

class PadreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Padre
        fields="__all__"