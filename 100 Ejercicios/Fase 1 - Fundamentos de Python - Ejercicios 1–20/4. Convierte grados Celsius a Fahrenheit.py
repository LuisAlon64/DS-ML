# Convierte grados Celsius a Fahrenheit
C = float(input("Introduce una cantidad de grados Celsius: "))

def conversor_a_Fahrenheit(grados_Celsius):
    F = grados_Celsius*(10/9)
    return F

print("La cantidad de grados Fahrenheit es: ", conversor_a_Fahrenheit(C), "F°")