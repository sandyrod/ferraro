from django.db import models

class Insumo(models.Model):
    name = models.CharField('Nombre', max_length = 255)
    description = models.CharField('Descripcion', max_length=255, blank=True, null=True)
    valor = models.FloatField('valor',  max_length=255, blank=True, null=True)
    unidad = models.BigIntegerField('unidad',  max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Insumos'
        verbose_name_plural = 'Insumos'

    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return f'{self.name}'