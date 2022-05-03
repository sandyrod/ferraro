from unicodedata import name
from django.urls import path
from apps.users.api.api import UserAPIView, UserDetailAPIView, UserValidate, GenerateTokenManuallyAPIView
from apps.users.api.api import UsersByGroupAPIView
urlpatterns = [
    path('usuario/', UserAPIView.as_view(), name = 'usuario_api'),
    path('usuario/<int:pk>/', UserDetailAPIView.as_view(), name = 'usuario_api'),
    path('usuario/bytoken/', UserValidate.as_view(), name='usuario_token'),
    path('usuario/gettoken/<int:pk>/', GenerateTokenManuallyAPIView.as_view(), name="usuario_gettoken"),
    path('usuario/operarios/', UsersByGroupAPIView.as_view(), name="usuarios por grupo")

]