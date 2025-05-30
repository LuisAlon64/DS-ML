a = int(input("Introduce un número: "))
b = int(input("Introduce otro número: "))

try:
    resultado = a / b
    print(f"El resultado de la división es: {resultado}")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")