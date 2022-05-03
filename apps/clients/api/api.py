from rest_framework.response import Response
from rest_framework.views import APIView
from apps.clients.models import Client
from apps.clients.api.serializers import ClientSerializer
from rest_framework.permissions import IsAuthenticated

class ClientAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        clients = Client.objects.all()
        clients_serializer = ClientSerializer(clients, many = True)
        return Response(clients_serializer.data)

    def post(self, request):
        clients_serializer = ClientSerializer(data = request.data)
        if clients_serializer.is_valid():
            clients_serializer.save()
            return Response(clients_serializer.data)
        return Response(clients_serializer.errors, status=400)

class ClientDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk=None):
        client = Client.objects.filter(id = pk).first()
        client_serializer = ClientSerializer(client)
        return Response(client_serializer.data)
    
    def put(self, request, pk):
        client = Client.objects.filter(id=pk).first()
        client_serializer = ClientSerializer(client, data=request.data)
        if client_serializer.is_valid():
            client_serializer.save()
            return Response(client_serializer.data)
        return Response(client_serializer.errors, status=400)

    def delete(self, request, pk):
        client = Client.objects.filter(id = pk).first()
        client.delete()
        return Response("Eliminado")