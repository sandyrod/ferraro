# Generated by Django 4.0.2 on 2022-05-23 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Motivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Motivos',
                'verbose_name_plural': 'Motivos',
            },
        ),
    ]
