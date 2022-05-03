from django.db import models

from simple_history.models import HistoricalRecords

class Material(models.Model):
    name = models.CharField('Material', max_length = 255)
    provider = models.BigIntegerField(null= True, blank=True)
    detail = models.TextField('Detalles', max_length = 255, blank = True, null = True)
    quantity = models.FloatField('Cantidad')
    historical = HistoricalRecords()

    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materiales'

    REQUIRED_FIELDS = ['name','quantity']

    def __str__(self):
        return f'{self.name}'