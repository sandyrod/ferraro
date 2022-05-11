from django.urls import path
from apps.instrumentos.api.api import InstrumentoAPIView
from apps.instrumentos.api.api import InstrumentoDetailAPIView

urlpatterns = [
    path('instrumento/', InstrumentoAPIView.as_view(), name = 'instrumento'),
    path('instrumento/<int:pk>/', InstrumentoDetailAPIView.as_view(), name = 'instrumento_api')
]