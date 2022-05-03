from django.db import models
from simple_history.models import HistoricalRecords

class Provider(models.Model):
    name = models.CharField('Nombre o Razon social', max_length = 255)
    cuit = models.CharField('CUIT', max_length= 15, unique=True)
    iibb = models.CharField('IIBB', max_length= 15, unique=True)
    email = models.EmailField('Correo Electrónico',max_length = 255, unique = True,)
    address = models.TextField('Direccion Fiscal', max_length = 255, blank = True, null = True)
    location = models.CharField('Localidad', max_length = 255, blank = True, null = True)
    postalcode = models.CharField('Codigo Postal', max_length=8, blank= True, null = True)
    province = models.CharField('Provincia', max_length=50, blank=True, null=True)
    web = models.URLField('Sitio Web', max_length=250, blank=True, null=True)
    phone = models.CharField('Telefono', max_length= 15, blank=True, null=True)
    contact = models.CharField('Contacto', max_length=255, blank=True, null=True)
    historical = HistoricalRecords()

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    REQUIRED_FIELDS = ['email','name','cuit']

    def __str__(self):
        return f'{self.name} {self.cuit}'


