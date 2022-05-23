from rest_framework import serializers
from apps.motivos.models import Motivo

class MotivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motivo
        fields = '__all__'