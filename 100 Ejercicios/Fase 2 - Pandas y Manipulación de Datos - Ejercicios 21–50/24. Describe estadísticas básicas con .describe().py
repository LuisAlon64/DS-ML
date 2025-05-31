import pandas as pd
data = {
    'Nombre': ['Alice', 'Bob', 'Charlie'],
    'Edad': [25, 30, 35],
    'Ciudad': ['New York', 'Los Angeles', 'Chicago'],
    'Salario': [70000, 80000, 90000]
}

df = pd.DataFrame(data)

# Describe estadísticas básicas del DataFrame
df_describe = df.describe()

# Imprime las estadísticas descriptivas del DataFrame
print(df_describe)