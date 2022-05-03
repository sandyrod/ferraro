from rest_framework.response import Response
from rest_framework.views import APIView
from apps.users.models import User
from django.contrib.auth.models import Group
from apps.users.api.serializers import UserSerializer, UserByGroupSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

class GenerateTokenManuallyAPIView(APIView):
    def get(self,request, pk=None):
        user = User.objects.filter(id = pk).first()
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

class UserAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        users = User.objects.all()
        users_serializer = UserSerializer(users, many = True)
        return Response(users_serializer.data)

    def post(self, request):
        users_serializer = UserSerializer(data = request.data)
        if users_serializer.is_valid():
            users_serializer.save()
            return Response(users_serializer.data)
        return Response(users_serializer.errors, status=400)

class UserDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk=None):
        user = User.objects.filter(id = pk).first()
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)
        #return Response(user_serializer.errors)
        
    def put(self, request, pk):
        user = User.objects.filter(id = pk).first()
        user_serializer = UserSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors, status=400)

    def delete(self, request, pk):
        user = User.objects.filter(id = pk).first()
        user.delete()
        return Response("Eliminado")

class UserValidate(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        #content = {'user_id' : str(request.user.id)}
        user = User.objects.filter(id = str(request.user.id)).first()
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)
        #return Response(content)

class UsersByGroupAPIView(APIView):
    def get(self, request):
        users = User.objects.filter(groups__name='operarios')
        users_serializer = UserByGroupSerializer(users, many = True)
        return Response(users_serializer.data)