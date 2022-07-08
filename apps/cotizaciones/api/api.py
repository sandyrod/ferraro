from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt import views as jwt_views
from apps.cotizaciones.models import Cotizacion, CotizacionDetail
from apps.cotizaciones.api.serializers import CotizacionSerializer, CotizacionDetailSerializer, CotizacionesWithDetailsListadoSerializer, CotizacionesWithDetailsSerializer
from rest_framework.permissions import IsAuthenticated

class CotizacionAPIView(APIView):
    #permission_classes = [IsAuthenticated]
    def get(self, request):
        cotizaciones = Cotizacion.objects.all().prefetch_related('cotizacion')
        cotizaciones_serializer = CotizacionesWithDetailsSerializer(cotizaciones, many = True)
        return Response(cotizaciones_serializer.data)

    def post(self, request):
        cotizaciones_serializer = CotizacionesWithDetailsListadoSerializer(data=request.data)
        if cotizaciones_serializer.is_valid():
            import copy

            cotizacion = cotizaciones_serializer.validated_data.copy()
            productos = cotizacion.pop('cotizacion')

            cotizacionmodel = Cotizacion(**cotizacion)
            cotizacionmodel.save()

            for datos in productos:
                detallenuevo = CotizacionDetail.objects.create(cotizacion = cotizacionmodel, **datos)

            return Response(cotizaciones_serializer.data, status=201)
        return Response(cotizaciones_serializer.errors, status=400)
        # cotizaciones_serializer = CotizacionSerializer(data = request.data)
        # if cotizaciones_serializer.is_valid():
        #     cotizaciones_serializer.save()
        #     return Response(cotizaciones_serializer.data)
        # return Response(cotizaciones_serializer.errors, status=400)

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
