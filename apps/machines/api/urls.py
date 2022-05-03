from unicodedata import name
from django.urls import  URLPattern, path
from apps.machines.api.api import MachineAPIView
from apps.machines.api.api import MachineDetailAPIView, MachineMantenimientoAPIView

urlpatterns = [
    path('maquinaria/', MachineAPIView.as_view(), name = 'maquinaria'),
    path('maquinaria/<int:pk>/', MachineDetailAPIView.as_view(), name = 'maquinaria_api'),
    path('maquinariamantenimiento/<int:pk>/', MachineMantenimientoAPIView.as_view(), name='maquinaria_mantenimiento')
]