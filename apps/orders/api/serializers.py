from dataclasses import field
from rest_framework import serializers
from apps.orders.models import Order, Otihistory
from apps.machines.api.serializers import MachineSerializer
from apps.materials.api.serializers import MaterialSerializer

class OrderSerializerRel(serializers.ModelSerializer):
    machine_id = MachineSerializer(many=False, read_only=False)
    material = MaterialSerializer(many=False, read_only=False)
    class Meta:
        model = Order
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OtiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Otihistory
        fields = '__all__'