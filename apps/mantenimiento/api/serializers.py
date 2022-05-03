from rest_framework import serializers
from apps.mantenimiento.models import Mantenimiento
from apps.machines.api.serializers import MachineSerializer

class MantenimientoSerializer(serializers.ModelSerializer):
    machine = MachineSerializer(many=False, read_only=False)
    class Meta:
        model = Mantenimiento
        fields = '__all__'

class MantenimientoMinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mantenimiento
        fields = '__all__'