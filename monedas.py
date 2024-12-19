def obtener_cambios(billete, denominaciones, cambio_actual=None, resultado=None):
    if cambio_actual is None:
        cambio_actual = []
    if resultado is None:
        resultado = []

    # Si el billete llega a 0, se agrega la combinación actual al resultado
    if billete == 0:
        resultado.append(cambio_actual)
        return resultado
    
    # Si el billete es menor a 0, no es una combinación válida
    if billete < 0:
        return resultado

    # Recorrer todas las denominaciones
    for i, denominacion in enumerate(denominaciones):
        obtener_cambios(billete - denominacion, denominaciones[i:], cambio_actual + [denominacion], resultado)

    return resultado

# Denominaciones mexicanas de billetes y monedas
denominaciones_mexicanas = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]  # Incluyendo monedas

# Solicitar el billete al usuario
try:
    billete = float(input("Introduce el valor del billete (en pesos): "))
    if billete not in denominaciones_mexicanas:
        print("Por favor, introduce un valor válido de billete.")
    else:
        print("Calculando todos los cambios posibles...\n")
        cambios = obtener_cambios(billete, denominaciones_mexicanas)
        print(f"Se encontraron {len(cambios)} combinaciones:")
        for i, cambio in enumerate(cambios, 1):
            print(f"{i}: {cambio}")
except ValueError:
    print("Por favor, introduce un número válido.")

