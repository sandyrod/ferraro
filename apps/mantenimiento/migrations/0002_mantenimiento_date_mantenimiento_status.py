# Generated by Django 4.0.3 on 2022-04-13 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimiento', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mantenimiento',
            name='date',
            field=models.TimeField(blank=True, null=True, verbose_name='Fecha'),
        ),
        migrations.AddField(
            model_name='mantenimiento',
            name='status',
            field=models.BooleanField(blank=True, null=True, verbose_name='Estatus'),
        ),
    ]
