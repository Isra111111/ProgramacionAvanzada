# Generated by Django 5.1.4 on 2024-12-18 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dron', '0002_movimiento'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Acelerometro',
        ),
        migrations.DeleteModel(
            name='Camara',
        ),
        migrations.DeleteModel(
            name='ControladorDron',
        ),
        migrations.DeleteModel(
            name='Giroscopio',
        ),
        migrations.DeleteModel(
            name='GPS',
        ),
        migrations.AddField(
            model_name='movimiento',
            name='acelerometro_x',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='movimiento',
            name='acelerometro_y',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='movimiento',
            name='acelerometro_z',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='movimiento',
            name='camara_fps',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='movimiento',
            name='giroscopio_x',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='movimiento',
            name='giroscopio_y',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='movimiento',
            name='giroscopio_z',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='movimiento',
            name='gps_lat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='movimiento',
            name='gps_lon',
            field=models.FloatField(null=True),
        ),
    ]