# Generated by Django 4.0.3 on 2022-03-21 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_otihistory_historicalorder_tratamiento_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otihistory',
            name='detail',
            field=models.TextField(blank=True, null=True, verbose_name='Observacion'),
        ),
    ]
