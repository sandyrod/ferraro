# Generated by Django 4.0.3 on 2022-04-13 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
        ('orders', '0006_alter_historicalorder_machine_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalorder',
            name='material',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='materials.material'),
        ),
        migrations.AddField(
            model_name='order',
            name='material',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.material'),
        ),
    ]
