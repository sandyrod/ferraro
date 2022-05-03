from django.db import models

from simple_history.models import HistoricalRecords

class Machine(models.Model):
    name = models.CharField('Nombre', max_length = 255)
    historical = HistoricalRecords()

    class Meta:
        verbose_name = 'Maquinaria'
        verbose_name_plural = 'Maquinarias'

    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return f'{self.name}'