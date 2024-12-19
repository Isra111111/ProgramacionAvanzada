# Generated by Django 5.1.4 on 2024-12-18 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dron', '0004_alter_movimiento_acelerometro_x_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movimiento',
            old_name='timestamp',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='movimiento',
            old_name='camara_fps',
            new_name='gps_alt',
        ),
        migrations.RenameField(
            model_name='movimiento',
            old_name='gps_lon',
            new_name='gps_long',
        ),
        migrations.RemoveField(
            model_name='movimiento',
            name='comando',
        ),
        migrations.AddField(
            model_name='movimiento',
            name='cam_vision',
            field=models.CharField(default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='movimiento',
            name='posicion_x',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='movimiento',
            name='posicion_y',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='movimiento',
            name='posicion_z',
            field=models.FloatField(default=0.0),
        ),
    ]