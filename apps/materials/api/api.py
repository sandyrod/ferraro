from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt import views as jwt_views
from apps.materials.models import Material
from apps.materials.api.serializers import MaterialSerializer
from rest_framework.permissions import IsAuthenticated

class MaterialAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        materials = Material.objects.all()
        materials_serializer = MaterialSerializer(materials, many = True)
        return Response(materials_serializer.data)

    def post(self, request):
        materials_serializer = MaterialSerializer(data = request.data)
        if materials_serializer.is_valid():
            materials_serializer.save()
            return Response(materials_serializer.data)
        return Response(materials_serializer.errors, status=400)

class MaterialDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk=None):
        material = Material.objects.filter(id = pk).first()
        material_serializer = MaterialSerializer(material)
        return Response(material_serializer.data)
    
    def put(self, request, pk):
        material = Material.objects.filter(id=pk).first()
        material_serializer = MaterialSerializer(material, data=request.data)
        if material_serializer.is_valid():
            material_serializer.save()
            return Response(material_serializer.data)
        return Response(material_serializer.errors, status=400)

    def delete(self, request, pk):
        material = Material.objects.filter(id = pk).first()
        material.delete()
        return Response("Eliminado")