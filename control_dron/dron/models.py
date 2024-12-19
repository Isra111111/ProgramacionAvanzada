from django.db import models

class Movimiento(models.Model):
    posicion_x = models.FloatField()
    posicion_y = models.FloatField()
    posicion_z = models.FloatField()
    acelerometro_x = models.FloatField()
    acelerometro_y = models.FloatField()
    acelerometro_z = models.FloatField()
    giroscopio_x = models.FloatField()
    giroscopio_y = models.FloatField()
    giroscopio_z = models.FloatField()
    camera_x = models.FloatField()
    camera_y = models.FloatField()
    gps_lat = models.FloatField()
    gps_lon = models.FloatField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Movimiento en {self.fecha}"