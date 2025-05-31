import csv
import pandas as pd

# Lee un archivo CSV y muestra las primeras 5 filas
with open("22_Ejercicio.csv", "r") as ej:
    lector = pd.read_csv(ej)
    print(lector.iloc[:5])  # Muestra las primeras 5 filas del archivo CSV