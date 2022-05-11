from rest_framework import serializers
from apps.piezas.models import Pieza

class PiezaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pieza
        fields = '__all__'