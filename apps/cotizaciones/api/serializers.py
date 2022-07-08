from dataclasses import field
from rest_framework import serializers
from apps.cotizaciones.models import Cotizacion, CotizacionDetail
from apps.machines.api.serializers import MachineSerializer
from apps.materials.api.serializers import MaterialSerializer

#class OrderSerializerRel(serializers.ModelSerializer):
#    plano = MachineSerializer(many=False, read_only=False)
#    cliente = MaterialSerializer(many=False, read_only=False)
#    class Meta:
#        model = Order
#        fields = '__all__'

class CotizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cotizacion
        fields = '__all__'

class CotizacionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CotizacionDetail
        fields = '__all__'

class CotizacionesWithDetailsSerializer(serializers.ModelSerializer):
    detalles = CotizacionDetailSerializer(many = True, source = 'cotizacion_id')
    class Meta:
        model = Cotizacion
        field='__all__'