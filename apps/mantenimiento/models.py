from django.db import models
from apps.machines.models import Machine

class Mantenimiento(models.Model):
    title = models.CharField('Titulo', max_length = 255)
    date = models.DateTimeField('Fecha', null=True, blank=True)
    machine = models.ForeignKey(Machine, null=True, blank=True, on_delete=models.CASCADE)
    status = models.BooleanField('Estatus', null=True, blank=True)
    color = models.CharField('Color', max_length= 255, null=True, blank=True)

    class Meta:
        verbose_name = 'Mantenimiento'
        verbose_name_plural = 'Mantenimientos'

    REQUIRED_FIELDS = ['title','date']

    def __str__(self):
        return f'{self.title}'