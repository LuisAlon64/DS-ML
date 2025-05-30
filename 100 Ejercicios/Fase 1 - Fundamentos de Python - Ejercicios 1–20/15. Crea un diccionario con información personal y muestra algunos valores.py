datos_personales = {
    "nombre": input("Introduce tu nombre: ").strip(),
    "edad": input("Introduce tu edad: ").strip(),
    "ciudad": input("Introduce tu ciudad: ").strip(),
    "profesion": input("Introduce tu profesión: ").strip(),
    "hobbies": input("Introduce tus hobbies (separados por comas): ").strip().split(",")
}
i = 0
while i == 0:
    quiere = input("¿Qué información quieres mostrar? (nombre, edad, ciudad, profesion, hobbies): ").strip().lower()
    if quiere in datos_personales:
        valor = datos_personales[quiere]
        print(f"{quiere.capitalize()}: {valor}")
    else:
        print("Información no encontrada.")
        continue
    