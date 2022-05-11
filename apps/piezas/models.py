from django.db import models

class Pieza(models.Model):
    name = models.CharField('Nombre', max_length = 255)
    description = models.CharField('Descripcion', max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Piezas'
        verbose_name_plural = 'Piezas'

    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return f'{self.name}'