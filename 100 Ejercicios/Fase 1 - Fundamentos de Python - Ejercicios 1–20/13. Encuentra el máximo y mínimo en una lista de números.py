lista_de_numeros = input("Ingrese una lista de números separados por comas: ").split(",")
lista_de_numeros = [int(num) for num in lista_de_numeros]  # Convertir a enteros
maximo = max(lista_de_numeros)  
minimo = min(lista_de_numeros)
print(f"El número máximo es: {maximo}")
print(f"El número mínimo es: {minimo}")