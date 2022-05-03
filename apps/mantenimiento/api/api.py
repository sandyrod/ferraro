from rest_framework.response import Response
from rest_framework.views import APIView
from apps.mantenimiento.models import Mantenimiento
from apps.mantenimiento.api.serializers import MantenimientoSerializer, MantenimientoMinSerializer
from rest_framework.permissions import IsAuthenticated

class MantenimientoAPIView(APIView):
    #permission_classes = [IsAuthenticated]
    def get(self, request):
        mantenimiento = Mantenimiento.objects.all()
        mantenimiento_serializer = MantenimientoSerializer(mantenimiento, many = True)
        return Response(mantenimiento_serializer.data)

    def post(self, request):
        mantenimiento_serializer = MantenimientoMinSerializer(data = request.data)
        if mantenimiento_serializer.is_valid():
            mantenimiento_serializer.save()
            return Response(mantenimiento_serializer.data)
        return Response(mantenimiento_serializer.errors, status=400)

class MantenimientoDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk=None):
        mantenimiento = Mantenimiento.objects.filter(id = pk).first()
        mantenimiento_serializer = MantenimientoSerializer(mantenimiento)
        return Response(mantenimiento_serializer.data)
    
    def put(self, request, pk):
        mantenimiento = Mantenimiento.objects.filter(id=pk).first()
        mantenimiento_serializer = MantenimientoMinSerializer(mantenimiento, data=request.data)
        if mantenimiento_serializer.is_valid():
            mantenimiento_serializer.save()
            return Response(mantenimiento_serializer.data)
        return Response(mantenimiento_serializer.errors, status=400)

    def delete(self, request, pk):
        mantenimiento = Mantenimiento.objects.filter(id = pk).first()
        mantenimiento.delete()
        return Response("Eliminado")