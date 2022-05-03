from unicodedata import name
from django.urls import  URLPattern, path
from apps.mantenimiento.api.api import MantenimientoAPIView
from apps.mantenimiento.api.api import MantenimientoDetailAPIView

urlpatterns = [
    path('mantenimiento/', MantenimientoAPIView.as_view(), name = 'mantenimiento'),
    path('mantenimiento/<int:pk>/', MantenimientoDetailAPIView.as_view(), name = 'mantenimiento_api')
]