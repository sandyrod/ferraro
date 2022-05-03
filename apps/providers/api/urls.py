from unicodedata import name
from django.urls import path
from apps.providers.api.api import ProviderAPIView
from apps.providers.api.api import ProviderDetailAPIView

urlpatterns = [
    path('proveedor/', ProviderAPIView.as_view(), name = 'proveedor'),
    path('proveedor/<int:pk>/', ProviderDetailAPIView.as_view(), name = 'proveedor_api')
]