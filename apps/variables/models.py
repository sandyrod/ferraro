from django.db import models

class Variable(models.Model):
    name = models.CharField('Nombre', max_length = 255)
    description = models.CharField('Descripcion', max_length=255, blank=True, null=True)
    valormax = models.CharField('valor maximo', max_length=255, blank=True, null=True)
    valormin = models.CharField('valor minimo', max_length=255, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Variables'
        verbose_name_plural = 'Variables'

    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return f'{self.name}'