from rest_framework.response import Response
from rest_framework.views import APIView
from apps.providers.models import Provider
from apps.providers.api.serializers import ProviderSerializer
from rest_framework.permissions import IsAuthenticated

class ProviderAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        providers = Provider.objects.all()
        providers_serializer = ProviderSerializer(providers, many = True)
        return Response(providers_serializer.data)

    def post(self, request):
        providers_serializer = ProviderSerializer(data = request.data)
        if providers_serializer.is_valid():
            providers_serializer.save()
            return Response(providers_serializer.data)
        return Response(providers_serializer.errors, status=400)

class ProviderDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk=None):
        provider = Provider.objects.filter(id = pk).first()
        provider_serializer = ProviderSerializer(provider)
        return Response(provider_serializer.data)
    
    def put(self, request, pk):
        provider = Provider.objects.filter(id=pk).first()
        provider_serializer = ProviderSerializer(provider, data=request.data)
        if provider_serializer.is_valid():
            provider_serializer.save()
            return Response(provider_serializer.data)
        return Response(provider_serializer.errors, status=400)

    def delete(self, request, pk):
        provider = Provider.objects.filter(id = pk).first()
        provider.delete()
        return Response("Eliminado")