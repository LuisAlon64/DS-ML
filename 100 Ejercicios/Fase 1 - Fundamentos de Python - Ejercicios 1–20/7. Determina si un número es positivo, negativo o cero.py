numero = float(input("Introduce un número: "))

def determinar(x):
    if x > 0:
        return "es positivo"
    elif x < 0:
        return "es negativo"
    else:
        return "es cero"
resultado = determinar(numero)
print(f"El número {numero} {resultado}.")