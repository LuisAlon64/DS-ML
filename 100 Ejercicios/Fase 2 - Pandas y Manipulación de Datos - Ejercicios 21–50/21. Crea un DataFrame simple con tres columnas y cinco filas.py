import pandas as pd

# Crea un DataFrame simple con tres columnas y cinco filas
data = {
    'Columna1': [1, 2, 3, 4, 5],
    'Columna2': ['A', 'B', 'C', 'D', 'E'],
    'Columna3': [True, False, True, False, True]
}
# Crea el DataFrame utilizando pandas
df = pd.DataFrame(data)

# Muestra el DataFrame
print(df)