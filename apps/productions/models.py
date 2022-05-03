from email.policy import default
from django.db import models
from simple_history.models import HistoricalRecords

class Production(models.Model):
    client = models.BigIntegerField('cliente_id', null=True, blank=True)
    number = models.CharField('codigo', max_length=20, blank=False, null=True)
    oc = models.BigIntegerField('Orden de compra', null= True, blank=True)
    cdolarpeso = models.FloatField('cotizacion peso dolar', null=True, blank=True)
    datein = models.DateField('fecha de ingreso', null=False, blank=False)
    dateout = models.DateField('fecha prevista', null=True, blank=True)
    detail = models.TextField('Detalles', max_length = 255, blank = True, null = True)
    piece = models.CharField('pieza', max_length=255, null=True, blank=True)
    quantity = models.FloatField('Cantidad', default=1)
    material = models.CharField('material', null=True, blank=True, max_length=255)
    tratamiento = models.BigIntegerField('tratamiento', null=True, blank=True)
    status = models.IntegerField('estatus', default=0)
    time = models.BigIntegerField('tiempo',default=0)
    obs = models.TextField('observaciones', null=True, blank=True)
    provider = models.BigIntegerField('provider_id', null=True, blank=True)
    currency = models.FloatField('Moneda', default=0)
    historical = HistoricalRecords()

    class Meta:
        verbose_name = 'Produccion'
        verbose_name_plural = 'Produccion'

    REQUIRED_FIELDS = ['client','datein']

    def __str__(self):
        return f'{self.id}'