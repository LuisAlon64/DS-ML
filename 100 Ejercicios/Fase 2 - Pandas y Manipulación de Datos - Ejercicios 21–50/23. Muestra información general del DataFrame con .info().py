import pandas as pd
data = {
    'Nombre': ['Alice', 'Bob', 'Charlie'],
    'Edad': [25, 30, 35],
    'Ciudad': ['New York', 'Los Angeles', 'Chicago'],
    'Salario': [70000, 80000, 90000]
}

df = pd.DataFrame(data)

# Muestra información general del DataFrame
df_info = df.info()

# Imprime la información del DataFrame
print(df_info)