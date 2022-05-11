from django.urls import path
from apps.planos.api.api import PlanoAPIView
from apps.planos.api.api import PlanoDetailAPIView

urlpatterns = [
    path('plano/', PlanoAPIView.as_view(), name = 'plano'),
    path('plano/<int:pk>/', PlanoDetailAPIView.as_view(), name = 'plano_api')
]