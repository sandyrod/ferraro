from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt import views as jwt_views
from apps.tratamiento.models import Tratamiento
from apps.tratamiento.api.serializers import TratamientoSerializer
from rest_framework.permissions import IsAuthenticated

class TratamientoAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tratamiento = Tratamiento.objects.all()
        tratamiento_serializer = TratamientoSerializer(tratamiento, many = True)
        return Response(tratamiento_serializer.data)

    def post(self, request):
        tratamiento_serializer = TratamientoSerializer(data = request.data)
        if tratamiento_serializer.is_valid():
            tratamiento_serializer.save()
            return Response(tratamiento_serializer.data)
        return Response(tratamiento_serializer.errors, status=400)

class TratamientoDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk=None):
        material = Tratamiento.objects.filter(id = pk).first()
        material_serializer = TratamientoSerializer(material)
        return Response(material_serializer.data)
    
    def put(self, request, pk):
        material = Tratamiento.objects.filter(id=pk).first()
        material_serializer = TratamientoSerializer(material, data=request.data)
        if material_serializer.is_valid():
            material_serializer.save()
            return Response(material_serializer.data)
        return Response(material_serializer.errors, status=400)

    def delete(self, request, pk):
        material = Tratamiento.objects.filter(id = pk).first()
        material.delete()
        return Response("Eliminado")