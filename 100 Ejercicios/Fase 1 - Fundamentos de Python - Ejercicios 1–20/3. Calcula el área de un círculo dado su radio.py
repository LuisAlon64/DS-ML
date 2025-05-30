# Calcula el área de un círculo dado su radio
radio = int(input("Introduce la medida del radio: "))

def area(r):
    area = r**2
    return area
print("El área del círculo es:", area(radio), "π")