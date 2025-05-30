palabra = input("Introduce una palabra o frase: ").strip().lower()
for letra in set(palabra):
    if letra.isalpha():  # Verifica si es una letra
        print(f"La letra '{letra}' aparece {palabra.count(letra)} veces.")
    else:
        print(f"'{letra}' no es una letra válida.")