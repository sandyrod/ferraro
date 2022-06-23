# Generated by Django 4.0.2 on 2022-06-23 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(blank=True, max_length=255, null=True, verbose_name='cliente')),
                ('moneda', models.BigIntegerField(blank=True, null=True, verbose_name='moneda')),
                ('impuesto', models.FloatField(blank=True, null=True, verbose_name='impuesto')),
                ('descuento', models.FloatField(blank=True, null=True, verbose_name='descuento')),
                ('validez', models.FloatField(blank=True, null=True, verbose_name='validez')),
                ('plazo', models.BigIntegerField(blank=True, null=True, verbose_name='plazo')),
                ('envio', models.FloatField(blank=True, null=True, verbose_name='envio')),
                ('observacion', models.CharField(blank=True, max_length=500, null=True, verbose_name='observacion')),
                ('planos', models.CharField(blank=True, max_length=255, null=True, verbose_name='plano')),
                ('empresa', models.BigIntegerField(blank=True, null=True, verbose_name='Empresa')),
                ('estado', models.CharField(blank=True, max_length=255, null=True, verbose_name='Estado')),
                ('fecha_entrega', models.DateField(blank=True, null=True, verbose_name='Fecha Entrega')),
            ],
            options={
                'verbose_name': 'Cotizacion',
                'verbose_name_plural': 'Cotizaciones',
            },
        ),
        migrations.CreateModel(
            name='CotizacionDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cotizacion_id', models.BigIntegerField(blank=True, null=True, verbose_name='Id de la cotizacion')),
                ('producto', models.BigIntegerField(blank=True, null=True, verbose_name='producto')),
                ('medida', models.FloatField(blank=True, null=True, verbose_name='medida')),
                ('cantidad', models.BigIntegerField(blank=True, null=True, verbose_name='tipo')),
                ('costo_unitario', models.BigIntegerField(blank=True, null=True, verbose_name='Usuario')),
                ('total', models.FloatField(blank=True, null=True, verbose_name='Total')),
            ],
            options={
                'verbose_name': 'Item Cotizacion',
                'verbose_name_plural': 'Items Cotizacion',
            },
        ),
    ]