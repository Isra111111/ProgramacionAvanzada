# Generated by Django 5.1.4 on 2024-12-18 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dron', '0006_sensor_rename_acelerometro_x_movimiento_distancia_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Sensor',
        ),
        migrations.RenameField(
            model_name='movimiento',
            old_name='distancia',
            new_name='acelerometro_x',
        ),
        migrations.RenameField(
            model_name='movimiento',
            old_name='duracion',
            new_name='acelerometro_y',
        ),
        migrations.RenameField(
            model_name='movimiento',
            old_name='timestamp',
            new_name='fecha',
        ),
        migrations.RemoveField(
            model_name='movimiento',
            name='direccion',
        ),
        migrations.AddField(
            model_name='movimiento',
            name='acelerometro_z',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='movimiento',
            name='cam_vision',
            field=models.CharField(default='Inactivo', max_length=50),
        ),
        migrations.AddField(
            model_name='movimiento',
            name='giroscopio_x',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='movimiento',
            name='giroscopio_y',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='movimiento',
            name='giroscopio_z',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='movimiento',
            name='gps_alt',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='movimiento',
            name='gps_lat',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='movimiento',
            name='gps_long',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='movimiento',
            name='posicion_x',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movimiento',
            name='posicion_y',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movimiento',
            name='posicion_z',
            field=models.IntegerField(default=0),
        ),
    ]
