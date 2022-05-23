from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt import views as jwt_views
from apps.planos.models import Plano
from apps.planos.api.serializers import PlanoSerializer
from rest_framework.permissions import IsAuthenticated

class PlanoAPIView(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request):
        planos = Plano.objects.all()
        planos_serializer = PlanoSerializer(planos, many = True)
        return Response(planos_serializer.data)

    def post(self, request):
        planos_serializer = PlanoSerializer(data = request.data)
        if planos_serializer.is_valid():
            planos_serializer.save()
            return Response(planos_serializer.data)
        return Response(planos_serializer.errors, status=400)

class PlanoDetailAPIView(APIView):
    #permission_classes = [IsAuthenticated]
    def get(self, request, pk=None):
        plano = Plano.objects.filter(id = pk).first()
        pieza_serializer = PlanoSerializer(plano)
        return Response(pieza_serializer.data)
    
    def put(self, request, pk):
        plano = Plano.objects.filter(id=pk).first()
        pieza_serializer = PlanoSerializer(plano, data=request.data)
        if pieza_serializer.is_valid():
            pieza_serializer.save()
            return Response(pieza_serializer.data)
        return Response(pieza_serializer.errors, status=400)

    def delete(self, request, pk):
        plano = Plano.objects.filter(id = pk).first()
        plano.delete()
        return Response("Eliminado")