# Generated by Django 4.0.2 on 2022-05-11 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instrumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Descripcion')),
                ('tipo', models.CharField(blank=True, max_length=255, null=True, verbose_name='tipo')),
                ('numero', models.CharField(blank=True, max_length=255, null=True, verbose_name='numero')),
            ],
            options={
                'verbose_name': 'Instrumentos',
                'verbose_name_plural': 'Instrumentos',
            },
        ),
    ]
