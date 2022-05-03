# Generated by Django 4.0.3 on 2022-03-04 00:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre o Razon social')),
                ('cuit', models.CharField(max_length=15, unique=True, verbose_name='CUIT')),
                ('iibb', models.CharField(max_length=15, unique=True, verbose_name='IIBB')),
                ('type_client', models.CharField(max_length=20, verbose_name='Tipo de Cliente')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Correo Electrónico')),
                ('address', models.TextField(blank=True, max_length=255, null=True, verbose_name='Direccion Fiscal')),
                ('location', models.CharField(blank=True, max_length=255, null=True, verbose_name='Localidad')),
                ('postalcode', models.CharField(blank=True, max_length=8, null=True, verbose_name='Codigo Postal')),
                ('province', models.CharField(blank=True, max_length=50, null=True, verbose_name='Provincia')),
                ('web', models.URLField(blank=True, max_length=250, null=True, verbose_name='Sitio Web')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefono')),
                ('contact', models.CharField(blank=True, max_length=255, null=True, verbose_name='Contacto')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
        migrations.CreateModel(
            name='HistoricalProvider',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre o Razon social')),
                ('cuit', models.CharField(db_index=True, max_length=15, verbose_name='CUIT')),
                ('iibb', models.CharField(db_index=True, max_length=15, verbose_name='IIBB')),
                ('type_client', models.CharField(max_length=20, verbose_name='Tipo de Cliente')),
                ('email', models.EmailField(db_index=True, max_length=255, verbose_name='Correo Electrónico')),
                ('address', models.TextField(blank=True, max_length=255, null=True, verbose_name='Direccion Fiscal')),
                ('location', models.CharField(blank=True, max_length=255, null=True, verbose_name='Localidad')),
                ('postalcode', models.CharField(blank=True, max_length=8, null=True, verbose_name='Codigo Postal')),
                ('province', models.CharField(blank=True, max_length=50, null=True, verbose_name='Provincia')),
                ('web', models.URLField(blank=True, max_length=250, null=True, verbose_name='Sitio Web')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefono')),
                ('contact', models.CharField(blank=True, max_length=255, null=True, verbose_name='Contacto')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Proveedor',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
