from django.db import models

class Plano(models.Model):
    name = models.CharField('Nombre', max_length = 255)
    description = models.CharField('Descripcion', max_length=255, blank=True, null=True)
    image = models.ImageField('plano', upload_to='planos/', max_length=255, null=True, blank = True)

    class Meta:
        verbose_name = 'Planos'
        verbose_name_plural = 'Planos'

    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return f'{self.name}'