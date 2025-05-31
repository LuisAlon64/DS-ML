import pandas as pd
data = {
    'Nombre': ['Alice', 'Bob', 'Charlie'],
    'Edad': [25, 30, 35],
    'Ciudad': ['New York', 'Los Angeles', 'Chicago'],
    'Salario': [70000, 80000, 90000]
}

df = pd.DataFrame(data)

df_columna = df[["Ciudad"]]  # Selecciona la columna "Ciudad" del DataFrame y la convierte en un nuevo DataFrame
print(df_columna)  # Imprime la columna seleccionada