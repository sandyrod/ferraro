from unicodedata import name
from django.urls import path
from apps.productions.api.api import ProductionAPIView
from apps.productions.api.api import ProductionDetailAPIView

urlpatterns = [
    path('produccion/', ProductionAPIView.as_view(), name = 'production'),
    path('produccion/<int:pk>/', ProductionDetailAPIView.as_view(), name = 'production_api')
]