from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dron/', include('dron.urls')),  # Incluye las rutas de la app 'dron'
    path('', include('dron.urls')),  # Redirige la raíz al inicio de la app
]