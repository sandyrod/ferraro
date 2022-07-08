from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt import views as jwt_views
from apps.cotizaciones.models import Cotizacion, CotizacionDetail
from apps.cotizaciones.api.serializers import CotizacionSerializer, CotizacionDetailSerializer, CotizacionesWithDetailsSerializer
from rest_framework.permissions import IsAuthenticated

class CotizacionAPIView(APIView):
    #permission_classes = [IsAuthenticated]
    def get(self, request):
        cotizaciones = Cotizacion.objects.all()
        cotizaciones_serializer = CotizacionesWithDetailsSerializer(cotizaciones, many = True)
        return Response(cotizaciones_serializer.data)

    def post(self, request):
        cotizaciones_serializer = CotizacionSerializer(data = request.data)
        if cotizaciones_serializer.is_valid():
            cotizaciones_serializer.save()
            return Response(cotizaciones_serializer.data)
        return Response(cotizaciones_serializer.errors, status=400)

class CotizacionDetailAPIView(APIView):
    #permission_classes = [IsAuthenticated]
    def get(self, request, pk=None):
        cotizacion = CotizacionDetail.objects.filter(id = pk).first()
        cotizacion_serializer = CotizacionDetailSerializer(cotizacion)
        return Response(cotizacion_serializer.data)
    
    def put(self, request, pk):
        cotizacion =CotizacionDetail.objects.filter(id=pk).first()
        cotizacion_serializer = CotizacionSerializer(cotizacion, data=request.data)
        if cotizacion_serializer.is_valid():
            cotizacion_serializer.save()
            return Response(cotizacion_serializer.data)
        return Response(cotizacion_serializer.errors, status=400)

    def delete(self, request, pk):
        cotizacion = CotizacionDetail.objects.filter(id = pk).first()
        cotizacion.delete()
        return Response("Eliminado")
