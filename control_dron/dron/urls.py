from django.urls import path
from . import views

urlpatterns = [
    path('', views.mover_dron, name='control_dron'),
    path('mover_dron/', views.mover_dron, name='mover_dron'),
    path('eliminar_movimiento/', views.eliminar_movimiento, name='eliminar_movimiento'),
]