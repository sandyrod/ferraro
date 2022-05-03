from rest_framework.response import Response
from rest_framework.views import APIView
from apps.insumos.models import Insumo
from apps.insumos.api.serializers import InsumoSerializer
from rest_framework.permissions import IsAuthenticated

class InsumoAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        insumo = Insumo.objects.all()
        insumo_serializer = InsumoSerializer(insumo, many = True)
        return Response(insumo_serializer.data)

    def post(self, request):
        insumo_serializer = InsumoSerializer(data = request.data)
        if insumo_serializer.is_valid():
            insumo_serializer.save()
            return Response(insumo_serializer.data)
        return Response(insumo_serializer.errors, status=400)

class InsumoDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk=None):
        insumo = Insumo.objects.filter(id = pk).first()
        insumo_serializer = InsumoSerializer(insumo)
        return Response(insumo_serializer.data)
    
    def put(self, request, pk):
        insumo = Insumo.objects.filter(id=pk).first()
        insumo_serializer = InsumoSerializer(insumo, data=request.data)
        if insumo_serializer.is_valid():
            insumo_serializer.save()
            return Response(insumo_serializer.data)
        return Response(insumo_serializer.errors, status=400)

    def delete(self, request, pk):
        insumo = Insumo.objects.filter(id = pk).first()
        insumo.delete()
        return Response("Eliminado")

class InsumoMantenimientoAPIView(APIView):
    def get(self, request, pk=None):
        mantenimiento = Mantenimiento.objects.filter(insumo=pk)
        mantenimiento_serializer = MantenimientoSerializer(mantenimiento, many = True)
        return Response(mantenimiento_serializer.data)