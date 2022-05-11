from django.db import models

class Instrumento(models.Model):
    name = models.CharField('Nombre', max_length = 255)
    description = models.CharField('Descripcion', max_length=255, blank=True, null=True)
    tipo = models.CharField('tipo', max_length=255, blank=True, null=True)
    numero = models.CharField('numero', max_length=255, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Instrumentos'
        verbose_name_plural = 'Instrumentos'

    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return f'{self.name}'