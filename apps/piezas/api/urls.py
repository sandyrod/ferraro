from django.urls import path
from apps.piezas.api.api import PiezaAPIView
from apps.piezas.api.api import PiezaDetailAPIView

urlpatterns = [
    path('pieza/', PiezaAPIView.as_view(), name = 'pieza'),
    path('pieza/<int:pk>/', PiezaDetailAPIView.as_view(), name = 'pieza_api')
]