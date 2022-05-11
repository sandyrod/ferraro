from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt import views as jwt_views
from apps.variables.models import Variable
from apps.variables.api.serializers import VariableSerializer
from rest_framework.permissions import IsAuthenticated

class VariableAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        variables = Variable.objects.all()
        variables_serializer = VariableSerializer(variables, many = True)
        return Response(variables_serializer.data)

    def post(self, request):
        variables_serializer = VariableSerializer(data = request.data)
        if variables_serializer.is_valid():
            variables_serializer.save()
            return Response(variables_serializer.data)
        return Response(variables_serializer.errors, status=400)

class VariableDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk=None):
        variable = Variable.objects.filter(id = pk).first()
        variable_serializer = VariableSerializer(variable)
        return Response(variable_serializer.data)
    
    def put(self, request, pk):
        variable = Variable.objects.filter(id=pk).first()
        variable_serializer = VariableSerializer(variable, data=request.data)
        if variable_serializer.is_valid():
            variable_serializer.save()
            return Response(variable_serializer.data)
        return Response(variable_serializer.errors, status=400)

    def delete(self, request, pk):
        variable = Variable.objects.filter(id = pk).first()
        variable.delete()
        return Response("Eliminado")