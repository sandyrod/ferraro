# Generated by Django 4.0.3 on 2022-03-04 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalprovider',
            name='type_client',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='type_client',
        ),
    ]
