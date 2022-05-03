from unicodedata import name
from django.urls import path
from apps.materials.api.api import MaterialAPIView
from apps.materials.api.api import MaterialDetailAPIView

urlpatterns = [
    path('material/', MaterialAPIView.as_view(), name = 'material'),
    path('material/<int:pk>/', MaterialDetailAPIView.as_view(), name = 'material_api')
]