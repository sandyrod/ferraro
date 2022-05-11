from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt import views as jwt_views
from apps.instrumentos.models import Instrumento
from apps.instrumentos.api.serializers import InstrumentoSerializer
from rest_framework.permissions import IsAuthenticated

class InstrumentoAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        instrumentos = Instrumento.objects.all()
        instrumentos_serializer = InstrumentoSerializer(instrumentos, many = True)
        return Response(instrumentos_serializer.data)

    def post(self, request):
        instrumentos_serializer = InstrumentoSerializer(data = request.data)
        if instrumentos_serializer.is_valid():
            instrumentos_serializer.save()
            return Response(instrumentos_serializer.data)
        return Response(instrumentos_serializer.errors, status=400)

class InstrumentoDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk=None):
        instrumento = Instrumento.objects.filter(id = pk).first()
        instrumento_serializer = InstrumentoSerializer(instrumento)
        return Response(instrumento_serializer.data)
    
    def put(self, request, pk):
        instrumento = Instrumento.objects.filter(id=pk).first()
        instrumento_serializer = InstrumentoSerializer(instrumento, data=request.data)
        if instrumento_serializer.is_valid():
            instrumento_serializer.save()
            return Response(instrumento_serializer.data)
        return Response(instrumento_serializer.errors, status=400)

    def delete(self, request, pk):
        instrumento = Instrumento.objects.filter(id = pk).first()
        instrumento.delete()
        return Response("Eliminado")