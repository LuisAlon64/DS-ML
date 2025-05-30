numero = int(input("Introduce un número natural para calcular su factorial: "))

def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
resultado = factorial(numero)
print(f"El factorial de {numero} es: {resultado}")