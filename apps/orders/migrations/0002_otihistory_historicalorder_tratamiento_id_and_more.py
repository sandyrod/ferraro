# Generated by Django 4.0.3 on 2022-03-21 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Otihistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oti_id', models.BigIntegerField(blank=True, null=True, verbose_name='Id de la orden')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Fecha')),
                ('time', models.FloatField(blank=True, null=True, verbose_name='Tiempo')),
                ('type', models.BigIntegerField(blank=True, null=True, verbose_name='tipo')),
                ('user_id', models.BigIntegerField(blank=True, null=True, verbose_name='Usuario')),
                ('detail', models.TimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Oti History',
                'verbose_name_plural': 'Otis History',
            },
        ),
        migrations.AddField(
            model_name='historicalorder',
            name='tratamiento_id',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Id de la maquinaria'),
        ),
        migrations.AddField(
            model_name='order',
            name='tratamiento_id',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Id de la maquinaria'),
        ),
        migrations.AlterField(
            model_name='historicalorder',
            name='machine_id',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Id de la maquinaria'),
        ),
        migrations.AlterField(
            model_name='historicalorder',
            name='number',
            field=models.FloatField(blank=True, null=True, verbose_name='numero'),
        ),
        migrations.AlterField(
            model_name='historicalorder',
            name='piece',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='pieza'),
        ),
        migrations.AlterField(
            model_name='historicalorder',
            name='production_id',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Id Produccion'),
        ),
        migrations.AlterField(
            model_name='historicalorder',
            name='quantity',
            field=models.FloatField(blank=True, null=True, verbose_name='cantidad'),
        ),
        migrations.AlterField(
            model_name='historicalorder',
            name='time',
            field=models.FloatField(blank=True, null=True, verbose_name='tiempo'),
        ),
        migrations.AlterField(
            model_name='order',
            name='machine_id',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Id de la maquinaria'),
        ),
        migrations.AlterField(
            model_name='order',
            name='number',
            field=models.FloatField(blank=True, null=True, verbose_name='numero'),
        ),
        migrations.AlterField(
            model_name='order',
            name='piece',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='pieza'),
        ),
        migrations.AlterField(
            model_name='order',
            name='production_id',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Id Produccion'),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.FloatField(blank=True, null=True, verbose_name='cantidad'),
        ),
        migrations.AlterField(
            model_name='order',
            name='time',
            field=models.FloatField(blank=True, null=True, verbose_name='tiempo'),
        ),
    ]
