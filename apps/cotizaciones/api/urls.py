from unicodedata import name
from django.urls import path
from apps.cotizaciones.api.api import CotizacionAPIView, CotizacionDetailAPIView

urlpatterns = [
    path('cotizacion/', CotizacionAPIView.as_view(), name = 'Cotizaciones'),
    path('cotizacion/<int:pk>/', CotizacionAPIView.as_view(), name = 'Cotizacion_api'),
    path('cotizaciondetail/', CotizacionDetailAPIView.as_view(), name = 'Detalles de cotizacion'),
    path('cotizaciondetail/<int:pk>/', CotizacionDetailAPIView.as_view(), name = 'Cotizacion_api'),

]