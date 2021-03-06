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

class CotizacionesWithDetailsListadoSerializer(serializers.ModelSerializer):
    cotizacion = CotizacionDetailSerializer(many=True)

    class Meta:
        model = Cotizacion
        fields = ['id', 'cliente', 'moneda', 'descuento', 'cotizacion']

class CotizacionesWithDetailsSerializer(CotizacionesWithDetailsListadoSerializer):
    cotizacion = CotizacionDetailSerializer(many=True)