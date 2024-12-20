# Generated by Django 5.1.4 on 2024-12-18 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dron', '0005_rename_timestamp_movimiento_fecha_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
                ('valor', models.FloatField(default=0.0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='movimiento',
            old_name='acelerometro_x',
            new_name='distancia',
        ),
        migrations.RenameField(
            model_name='movimiento',
            old_name='acelerometro_z',
            new_name='duracion',
        ),
        migrations.RenameField(
            model_name='movimiento',
            old_name='fecha',
            new_name='timestamp',
        ),
        migrations.RemoveField(
            model_name='movimiento',
            name='acelerometro_y',
        ),
        migrations.RemoveField(
            model_name='movimiento',
            name='cam_vision',
        ),
        migrations.RemoveField(
            model_name='movimiento',
            name='giroscopio_x',
        ),
        migrations.RemoveField(
            model_name='movimiento',
            name='giroscopio_y',
        ),
        migrations.RemoveField(
            model_name='movimiento',
            name='giroscopio_z',
        ),
        migrations.RemoveField(
            model_name='movimiento',
            name='gps_alt',
        ),
        migrations.RemoveField(
            model_name='movimiento',
            name='gps_lat',
        ),
        migrations.RemoveField(
            model_name='movimiento',
            name='gps_long',
        ),
        migrations.RemoveField(
            model_name='movimiento',
            name='posicion_x',
        ),
        migrations.RemoveField(
            model_name='movimiento',
            name='posicion_y',
        ),
        migrations.RemoveField(
            model_name='movimiento',
            name='posicion_z',
        ),
        migrations.AddField(
            model_name='movimiento',
            name='direccion',
            field=models.CharField(default='Desconocido', max_length=50),
        ),
    ]
