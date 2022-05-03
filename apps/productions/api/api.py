from rest_framework.response import Response
from rest_framework.views import APIView
from apps.productions.models import Production
from apps.productions.api.serializers import ProductionSerializer
from rest_framework.permissions import IsAuthenticated

class ProductionAPIView(APIView):
    #permission_classes = [IsAuthenticated]
    def get(self, request):
        productions = Production.objects.all()
        productions_serializer = ProductionSerializer(productions, many = True)
        return Response(productions_serializer.data)

    def post(self, request):
        productions_serializer = ProductionSerializer(data = request.data)
        if productions_serializer.is_valid():
            productions_serializer.save()
            return Response(productions_serializer.data)
        return Response(productions_serializer.errors, status=400)

class ProductionDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk=None):
        production = Production.objects.filter(id = pk).first()
        production_serializer = ProductionSerializer(production)
        return Response(production_serializer.data)
    
    def put(self, request, pk):
        production = Production.objects.filter(id=pk).first()
        production_serializer = ProductionSerializer(production, data=request.data)
        if production_serializer.is_valid():
            production_serializer.save()
            return Response(production_serializer.data)
        return Response(production_serializer.errors, status=400)

    def delete(self, request, pk):
        production = Production.objects.filter(id = pk).first()
        production.delete()
        return Response("Eliminado")