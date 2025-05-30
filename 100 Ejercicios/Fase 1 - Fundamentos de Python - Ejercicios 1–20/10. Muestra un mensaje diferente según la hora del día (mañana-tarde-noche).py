hora = float(input("Introduce la hora (0-24): "))

def mensaje_hora(hora):
    if 6 <= hora < 12:
        return "¡Buenos días!"
    elif 12 <= hora < 18:
        return "¡Buenas tardes!"
    elif 18 <= hora < 24 or hora == 0:
        return "¡Buenas noches!"
    else:
        return "Hora no válida"
resultado = mensaje_hora(hora)
print(resultado)
# El programa solicita al usuario ingresar una hora y muestra un mensaje diferente según la hora del día.