from rest_framework import serializers
from apps.instrumentos.models import Instrumento

class InstrumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrumento
        fields = '__all__'