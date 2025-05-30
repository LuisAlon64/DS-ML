c1 = float(input("Ingrese la primera calificación: "))
c2 = float(input("Ingrese la segunda calificación: "))
c3 = float(input("Ingrese la tercera calificación: "))

def promedio(c1, c2, c3):
    return (c1 + c2 + c3) / 3
resultado = promedio(c1, c2, c3)
print(f"El promedio de las calificaciones es: {resultado:.2f}")
# El programa solicita al usuario ingresar tres calificaciones y calcula el promedio de estas.