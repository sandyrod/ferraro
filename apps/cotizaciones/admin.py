from django.contrib import admin
from apps.cotizaciones.models import Cotizacion, CotizacionDetail

# Register your models here.
admin.site.register(Cotizacion)
admin.site.register(CotizacionDetail)