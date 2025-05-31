import pandas as pd
data = {
    'Nombre': ['Alice', 'Bob', 'Charlie'],
    'Edad': [25, 30, 35],
    'Ciudad': ['New York', 'Los Angeles', 'Chicago'],
    'Salario': [30, 100, 150]
}

df = pd.DataFrame(data)

df_filtrado = df[df['Salario'] > 100]  # Filtra las filas donde la columna 'Salario' tiene valores mayores a 100
print(df_filtrado)  # Imprime el DataFrame filtrado