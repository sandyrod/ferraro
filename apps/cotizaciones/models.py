from statistics import mode
from django.db import models

class Cotizacion(models.Model):
    cliente = models.CharField('cliente',  max_length=255, blank=True, null=True)
    moneda = models.BigIntegerField('moneda', blank=True, null=True)
    impuesto = models.FloatField('impuesto', blank=True, null=True)
    descuento = models.FloatField('descuento', blank=True, null=True)
    validez = models.FloatField('validez', blank=True, null=True)
    plazo = models.BigIntegerField('plazo', blank=True, null=True)
    envio = models.FloatField('envio', blank=True, null=True)
    observacion = models.CharField('observacion', max_length=500, blank=True, null=True)
    planos = models.CharField('plano', max_length=255, blank=True, null=True)
    empresa = models.BigIntegerField('Empresa', blank=True, null=True)
    estado = models.CharField('Estado',  max_length=255, blank=True, null=True)
    fecha_entrega = models.DateField('Fecha Entrega', blank=True, null=True)
    

    class Meta:
        verbose_name = 'Cotizacion'
        verbose_name_plural = 'Cotizaciones'

    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return f'{self.cliente}'

class CotizacionDetail(models.Model):
    cotizacion_id = models.BigIntegerField('Id de la cotizacion', null=True, blank=True)
    producto = models.BigIntegerField('producto', null=True, blank=True)
    medida = models.FloatField('medida', null=True, blank=True)
    cantidad = models.BigIntegerField('cantidad', null=True, blank=True)
    costo_unitario = models.BigIntegerField('costo unitario', null=True, blank=True)
    total = models.FloatField('Total', null=True, blank=True)

    class Meta:
        verbose_name = 'Item Cotizacion'
        verbose_name_plural = 'Items Cotizacion'
    
    #REQUIRED_FIELDS = ['']

    def __str__(self):
        return f'{self.id}'