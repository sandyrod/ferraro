from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt import views as jwt_views
from apps.piezas.models import Pieza
from apps.piezas.api.serializers import PiezaSerializer
from rest_framework.permissions import IsAuthenticated

class PiezaAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        piezas = Pieza.objects.all()
        piezas_serializer = PiezaSerializer(piezas, many = True)
        return Response(piezas_serializer.data)

    def post(self, request):
        piezas_serializer = PiezaSerializer(data = request.data)
        if piezas_serializer.is_valid():
            piezas_serializer.save()
            return Response(piezas_serializer.data)
        return Response(piezas_serializer.errors, status=400)

class PiezaDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk=None):
        pieza = Pieza.objects.filter(id = pk).first()
        pieza_serializer = PiezaSerializer(pieza)
        return Response(pieza_serializer.data)
    
    def put(self, request, pk):
        pieza = Pieza.objects.filter(id=pk).first()
        pieza_serializer = PiezaSerializer(pieza, data=request.data)
        if pieza_serializer.is_valid():
            pieza_serializer.save()
            return Response(pieza_serializer.data)
        return Response(pieza_serializer.errors, status=400)

    def delete(self, request, pk):
        pieza = Pieza.objects.filter(id = pk).first()
        pieza.delete()
        return Response("Eliminado")