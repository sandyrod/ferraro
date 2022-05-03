from unicodedata import name
from django.urls import  URLPattern, path
from apps.insumos.api.api import InsumoAPIView
from apps.insumos.api.api import InsumoDetailAPIView

urlpatterns = [
    path('insumo/', InsumoAPIView.as_view(), name = 'insumo'),
    path('insumo/<int:pk>/', InsumoDetailAPIView.as_view(), name = 'insumo_api')
]