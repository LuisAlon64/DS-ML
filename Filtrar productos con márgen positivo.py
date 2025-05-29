import pandas as pd

data = {
    "Producto": ["A", "B", "C", "D"],
    "Ventas": [1000, 800, 1200, 900],
    "Costos": [800, 900, 1000, 950]
}
df = pd.DataFrame(data)
print(df)
df["Margen"] = df["Ventas"] - df["Costos"]
print(list(df["Margen"]))
lista = []
for m in list(df["Margen"]):
    if m > 0:
        lista.append(m)
print("Lista de márgenes positivos:", lista)