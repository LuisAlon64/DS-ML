numero = float(input("Introduce un número: "))

def par_impar(x):
    if x % 2 == 0:
        return "Es par!!!"
    else:
        return "Es impar!!!"
print(numero , par_impar(numero))