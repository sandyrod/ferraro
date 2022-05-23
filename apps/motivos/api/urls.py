from django.urls import path
from apps.motivos.api.api import MotivoAPIView, MotivoDetailAPIView

urlpatterns = [
    path('motivo/', MotivoAPIView.as_view(), name = 'motivo'),
    path('motivo/<int:pk>/', MotivoDetailAPIView.as_view(), name = 'motivo_api')
]