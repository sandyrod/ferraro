from platform import machine
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.machines.models import Machine
from apps.mantenimiento.models import Mantenimiento
from apps.machines.api.serializers import MachineSerializer
from apps.mantenimiento.api.serializers import MantenimientoSerializer
from rest_framework.permissions import IsAuthenticated

class MachineAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        machine = Machine.objects.all()
        machine_serializer = MachineSerializer(machine, many = True)
        return Response(machine_serializer.data)

    def post(self, request):
        machine_serializer = MachineSerializer(data = request.data)
        if machine_serializer.is_valid():
            machine_serializer.save()
            return Response(machine_serializer.data)
        return Response(machine_serializer.errors, status=400)

class MachineDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk=None):
        machine = Machine.objects.filter(id = pk).first()
        machine_serializer = MachineSerializer(machine)
        return Response(machine_serializer.data)
    
    def put(self, request, pk):
        machine = Machine.objects.filter(id=pk).first()
        machine_serializer = MachineSerializer(machine, data=request.data)
        if machine_serializer.is_valid():
            machine_serializer.save()
            return Response(machine_serializer.data)
        return Response(machine_serializer.errors, status=400)

    def delete(self, request, pk):
        machine = Machine.objects.filter(id = pk).first()
        machine.delete()
        return Response("Eliminado")

class MachineMantenimientoAPIView(APIView):
    def get(self, request, pk=None):
        mantenimiento = Mantenimiento.objects.filter(machine=pk)
        mantenimiento_serializer = MantenimientoSerializer(mantenimiento, many = True)
        return Response(mantenimiento_serializer.data)