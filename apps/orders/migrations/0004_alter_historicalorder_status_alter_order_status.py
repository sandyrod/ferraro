# Generated by Django 4.0.3 on 2022-04-08 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_otihistory_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalorder',
            name='status',
            field=models.BigIntegerField(default=0, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.BigIntegerField(default=0, verbose_name='Status'),
        ),
    ]
