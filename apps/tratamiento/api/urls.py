from unicodedata import name
from django.urls import path
from apps.tratamiento.api.api import TratamientoAPIView
from apps.tratamiento.api.api import TratamientoDetailAPIView

urlpatterns = [
    path('tratamiento/', TratamientoAPIView.as_view(), name = 'tratamiento'),
    path('tratamiento/<int:pk>/', TratamientoDetailAPIView.as_view(), name = 'tratamiento_api')
]