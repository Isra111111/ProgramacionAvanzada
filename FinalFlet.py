import flet as ft
from datetime import datetime

# Datos en memoria
movimientos = []
posicion = {"X": 0, "Y": 0, "Z": 0}
indice_global = 1  # Para asignar índices únicos a los movimientos

# Sensores simulados
sensores = {
    "giroscopio_x": 0.0,
    "giroscopio_y": 0.0,
    "giroscopio_z": 0.0,
    "acelerometro_x": 0.0,
    "acelerometro_y": 0.0,
    "acelerometro_z": 0.0,
    "camera_x": 0.0,
    "camera_y": 0.0,
    "gps_lat": 0.0,
    "gps_lon": 0.0,
    "presion": 1013.25,  # Presión atmosférica en hPa por defecto
}

# Función para mover el dron
def mover_dron(axis, sign):
    global indice_global
    # Actualizar la posición
    posicion[axis] += sign
    # Simular valores de sensores basados en la posición
    sensores["giroscopio_x"] = posicion["X"] * 0.9
    sensores["giroscopio_y"] = posicion["Y"] * 0.9
    sensores["giroscopio_z"] = posicion["Z"] * 0.9
    sensores["acelerometro_x"] = posicion["X"] * 1.1
    sensores["acelerometro_y"] = posicion["Y"] * 1.1
    sensores["acelerometro_z"] = posicion["Z"] * 1.1
    sensores["camera_x"] = posicion["X"] * 0.8
    sensores["camera_y"] = posicion["Y"] * 0.8
    sensores["gps_lat"] = 19.4326 + posicion["X"] * 0.001  # Simulando coordenadas GPS
    sensores["gps_lon"] = -99.1332 + posicion["Y"] * 0.001
    sensores["presion"] = 1013.25 - posicion["Z"] * 0.1  # Simulando altitud que afecta la presión

    # Guardar en historial
    movimientos.append(
        {
            "id": indice_global,
            "posicion_x": posicion["X"],
            "posicion_y": posicion["Y"],
            "posicion_z": posicion["Z"],
            "giroscopio_x": sensores["giroscopio_x"],
            "giroscopio_y": sensores["giroscopio_y"],
            "giroscopio_z": sensores["giroscopio_z"],
            "gps_lat": sensores["gps_lat"],
            "gps_lon": sensores["gps_lon"],
            "presion": sensores["presion"],
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
    )
    indice_global += 1

# Función para eliminar un movimiento por índice
def eliminar_movimiento(indice):
    global movimientos
    movimientos = [m for m in movimientos if m["id"] != indice]

# Función principal de Flet
def main(page: ft.Page):
    page.title = "Control de Dron con Sensores"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20

    # Valores iniciales
    posicion_x = ft.Text(value=str(posicion["X"]), size=20, weight=ft.FontWeight.BOLD)
    posicion_y = ft.Text(value=str(posicion["Y"]), size=20, weight=ft.FontWeight.BOLD)
    posicion_z = ft.Text(value=str(posicion["Z"]), size=20, weight=ft.FontWeight.BOLD)

    # Textos para sensores
    sensor_textos = {key: ft.Text(value=f"{value:.2f}", size=16) for key, value in sensores.items()}

    # Lista de historial con contenedor desplazable
    historial = ft.ListView(expand=1, spacing=10)

    # Campo para eliminar por índice
    eliminar_campo = ft.TextField(hint_text="Índice", expand=1, keyboard_type=ft.KeyboardType.NUMBER)

    # Actualizar historial de movimientos
    def actualizar_historial():
        historial.controls.clear()
        for mov in movimientos:
            historial.controls.append(
                ft.Text(
                    f"{mov['id']} | Posición: X={mov['posicion_x']} Y={mov['posicion_y']} Z={mov['posicion_z']} "
                    f"| Fecha: {mov['fecha']} | GPS: Lat={mov['gps_lat']:.4f}, Lon={mov['gps_lon']:.4f} | Presión: {mov['presion']:.2f} hPa",
                    size=14,
                )
            )
        page.update()

    # Actualizar valores de sensores
    def actualizar_sensores():
        for key, texto in sensor_textos.items():
            texto.value = f"{sensores[key]:.2f}"

    # Botón para mover el dron
    def boton_mover(axis, sign):
        mover_dron(axis, sign)
        posicion_x.value = str(posicion["X"])
        posicion_y.value = str(posicion["Y"])
        posicion_z.value = str(posicion["Z"])
        actualizar_historial()
        actualizar_sensores()
        page.update()

    # Botón para eliminar un movimiento
    def boton_eliminar(e):
        try:
            indice = int(eliminar_campo.value)
            eliminar_movimiento(indice)
            eliminar_campo.value = ""
            actualizar_historial()
        except ValueError:
            eliminar_campo.error_text = "Por favor ingresa un número válido."
            eliminar_campo.update()

    # Layout principal
    page.add(
        ft.Column(
            controls=[
                ft.Text("Control del Dron con Sensores", size=24, weight=ft.FontWeight.BOLD),
                ft.Row(
                    controls=[
                        ft.Text("Posición Actual: ", size=16),
                        ft.Text("X: ", size=16),
                        posicion_x,
                        ft.Text("Y: ", size=16),
                        posicion_y,
                        ft.Text("Z: ", size=16),
                        posicion_z,
                    ]
                ),
                ft.Text("Sensores", size=20, weight=ft.FontWeight.BOLD),
                ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Text("Giroscopio", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text(f"X: ", size=16),
                                sensor_textos["giroscopio_x"],
                                ft.Text(f"Y: ", size=16),
                                sensor_textos["giroscopio_y"],
                                ft.Text(f"Z: ", size=16),
                                sensor_textos["giroscopio_z"],
                            ]
                        ),
                        ft.Column(
                            controls=[
                                ft.Text("Acelerómetro", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text(f"X: ", size=16),
                                sensor_textos["acelerometro_x"],
                                ft.Text(f"Y: ", size=16),
                                sensor_textos["acelerometro_y"],
                                ft.Text(f"Z: ", size=16),
                                sensor_textos["acelerometro_z"],
                            ]
                        ),
                        ft.Column(
                            controls=[
                                ft.Text("Cámara", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text(f"X: ", size=16),
                                sensor_textos["camera_x"],
                                ft.Text(f"Y: ", size=16),
                                sensor_textos["camera_y"],
                            ]
                        ),
                        ft.Column(
                            controls=[
                                ft.Text("GPS", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text(f"Latitud: ", size=16),
                                sensor_textos["gps_lat"],
                                ft.Text(f"Longitud: ", size=16),
                                sensor_textos["gps_lon"],
                            ]
                        ),
                        ft.Column(
                            controls=[
                                ft.Text("Presión", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text(f"{sensor_textos['presion'].value} hPa", size=16),
                            ]
                        ),
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.ElevatedButton("Mover X+", on_click=lambda e: boton_mover("X", 1)),
                        ft.ElevatedButton("Mover X-", on_click=lambda e: boton_mover("X", -1)),
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.ElevatedButton("Mover Y+", on_click=lambda e: boton_mover("Y", 1)),
                        ft.ElevatedButton("Mover Y-", on_click=lambda e: boton_mover("Y", -1)),
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.ElevatedButton("Mover Z+", on_click=lambda e: boton_mover("Z", 1)),
                        ft.ElevatedButton("Mover Z-", on_click=lambda e: boton_mover("Z", -1)),
                    ]
                ),
                ft.Row(
                    controls=[
                        eliminar_campo,
                        ft.ElevatedButton("Eliminar Movimiento", on_click=boton_eliminar),
                    ]
                ),
                ft.Text("Historial de Movimientos", size=20, weight=ft.FontWeight.BOLD),
                historial,  
            ],
            expand=True,
        )
    )

    actualizar_historial()
    actualizar_sensores()

ft.app(target=main)
