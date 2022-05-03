from unicodedata import name
from django.urls import URLPattern, path
from apps.clients.api.api import ClientAPIView
from apps.clients.api.api import ClientDetailAPIView

urlpatterns = [
    path('cliente/', ClientAPIView.as_view(), name = 'cliente'),
    path('cliente/<int:pk>/', ClientDetailAPIView.as_view(), name = 'cliente_api')
]