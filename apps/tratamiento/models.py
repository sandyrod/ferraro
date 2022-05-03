from django.db import models

# Create your models here.

class Tratamiento(models.Model):
    name = models.CharField('Tratamiento', max_length = 255)
    detail = models.TextField('Detalles', max_length = 255, blank = True, null = True)

    class Meta:
        verbose_name = 'Tratamiento'
        verbose_name_plural = 'Tratamientos'

    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return f'{self.name}'