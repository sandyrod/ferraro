# Generated by Django 4.0.3 on 2022-04-21 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_historicalorder_material_order_material'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalorder',
            name='tratamiento_id',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='tratamiento'),
        ),
        migrations.AlterField(
            model_name='order',
            name='tratamiento_id',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='tratamiento'),
        ),
    ]
