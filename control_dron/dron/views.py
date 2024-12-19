from django.shortcuts import render, redirect
from .models import Movimiento
import random
from datetime import datetime

# Variables iniciales
posicion_x, posicion_y, posicion_z = 0.0, 0.0, 0.0

def control_dron(request):
    movimientos = Movimiento.objects.all().order_by('-fecha')
    sensores = {
        'acelerometro': [random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(-5, 5)],
        'giroscopio': [random.uniform(-180, 180), random.uniform(-180, 180), random.uniform(-180, 180)],
        'gps': [random.uniform(-90, 90), random.uniform(-180, 180)],
        'camera': [posicion_x * 0.5, posicion_y * 0.5],
    }
    context = {
        'movimientos': movimientos,
        'posicion_x': posicion_x,
        'posicion_y': posicion_y,
        'posicion_z': posicion_z,
        'sensores': sensores,
    }
    return render(request, 'dron/control_dron.html', context)

def mover_dron(request):
    global posicion_x, posicion_y, posicion_z

    axis = request.GET.get('axis')
    sign = int(request.GET.get('sign', 0))

    if axis == 'X':
        posicion_x += sign
    elif axis == 'Y':
        posicion_y += sign
    elif axis == 'Z':
        posicion_z += sign

    # Simula los valores de los sensores
    acelerometro_x, acelerometro_y, acelerometro_z = [random.uniform(-5, 5) for _ in range(3)]
    giroscopio_x, giroscopio_y, giroscopio_z = [random.uniform(-180, 180) for _ in range(3)]
    camera_x, camera_y = posicion_x * 0.5, posicion_y * 0.5
    gps_lat, gps_lon = random.uniform(-90, 90), random.uniform(-180, 180)

    # Registra el movimiento en la base de datos
    Movimiento.objects.create(
        posicion_x=posicion_x,
        posicion_y=posicion_y,
        posicion_z=posicion_z,
        acelerometro_x=acelerometro_x,
        acelerometro_y=acelerometro_y,
        acelerometro_z=acelerometro_z,
        giroscopio_x=giroscopio_x,
        giroscopio_y=giroscopio_y,
        giroscopio_z=giroscopio_z,
        camera_x=camera_x,
        camera_y=camera_y,
        gps_lat=gps_lat,
        gps_lon=gps_lon,
    )

    return control_dron(request)

def eliminar_movimiento(request):
    if request.method == 'POST':
        movimientos_ids = request.POST.getlist('movimientos')
        Movimiento.objects.filter(id__in=movimientos_ids).delete()
    return redirect('control_dron')