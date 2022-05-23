from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt import views as jwt_views
from apps.motivos.models import Motivo
from apps.motivos.api.serializers import MotivoSerializer
from rest_framework.permissions import IsAuthenticated

class MotivoAPIView(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request):
        motivos = Motivo.objects.all()
        motivos_serializer = MotivoSerializer(motivos, many = True)
        return Response(motivos_serializer.data)

    def post(self, request):
        motivos_serializer = MotivoSerializer(data = request.data)
        if motivos_serializer.is_valid():
            motivos_serializer.save()
            return Response(motivos_serializer.data)
        return Response(motivos_serializer.errors, status=400)

class MotivoDetailAPIView(APIView):
    #permission_classes = [IsAuthenticated]
    def get(self, request, pk=None):
        pieza = Motivo.objects.filter(id = pk).first()
        pieza_serializer = MotivoSerializer(pieza)
        return Response(pieza_serializer.data)
    
    def put(self, request, pk):
        pieza = Motivo.objects.filter(id=pk).first()
        pieza_serializer = MotivoSerializer(pieza, data=request.data)
        if pieza_serializer.is_valid():
            pieza_serializer.save()
            return Response(pieza_serializer.data)
        return Response(pieza_serializer.errors, status=400)

    def delete(self, request, pk):
        pieza = Motivo.objects.filter(id = pk).first()
        pieza.delete()
        return Response("Eliminado")