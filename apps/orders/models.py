from email.policy import default
from tabnanny import verbose
from django.db import models
from apps.machines.models import Machine
from apps.materials.models import Material
from simple_history.models import HistoricalRecords

class Order(models.Model):
    production_id = models.BigIntegerField('Id Produccion', null=True, blank=True)
    piece = models.CharField('pieza', max_length=255, null=True, blank=True)
    number = models.FloatField('numero', null=True, blank=True)
    quantity = models.FloatField('cantidad', null=True, blank=True)
    status = models.BigIntegerField('Status', default=0)
    current_operator = models.BigIntegerField('Operador Actual', null=True, blank=True)
    time = models.FloatField('tiempo', null=True, blank=True)
    total_time = models.FloatField('tiempo_total', null=True, blank=True)
    gcode = models.TextField('Detalles',  null = True)
    machine_id = models.ForeignKey(Machine, null=True, blank=True, on_delete=models.CASCADE)
    tratamiento_id = models.BigIntegerField('tratamiento', null=True, blank=True)
    pause = models.BigIntegerField('Motivo de pausada', null=True, blank=True)
    material = models.ForeignKey(Material, null=True, blank=True, on_delete=models.CASCADE)
    historical = HistoricalRecords()

    class Meta:
        verbose_name = 'Ordenes'
        verbose_name_plural = 'Ordenes'

    REQUIRED_FIELDS = ['client','datein']

    def __str__(self):
        return f'{self.id}'

class Otihistory(models.Model):
    oti_id = models.BigIntegerField('Id de la orden', null=True, blank=True)
    date = models.DateField('Fecha', null=True, blank=True)
    time = models.FloatField('Tiempo', null=True, blank=True)
    type = models.BigIntegerField('tipo', null=True, blank=True)
    user_id = models.BigIntegerField('Usuario', null=True, blank=True)
    detail = models.TextField('Observacion', null=True, blank=True)

    class Meta:
        verbose_name = 'Oti History'
        verbose_name_plural = 'Otis History'
    
    #REQUIRED_FIELDS = ['']

    def __str__(self):
        return f'{self.id}'