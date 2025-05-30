lista = [1, 2, 3, 4, 5]
print("Lista original:", lista)
# Agregar un elemento al final de la lista
lista.append(6)
print("Lista después de agregar un elemento al final:", lista)

# Agregar un elemento en una posición específica (índice 2)
lista.insert(2, 2.5)
print("Lista después de agregar un elemento en la posición 2:", lista)

# Eliminar un elemento por su valor
lista.remove(3)
print("Lista después de eliminar 'Elemento 3':", lista)

# Eliminar un elemento por su índice (índice 1)
lista.pop(1)
print("Lista después de eliminar el elemento en la posición 1:", lista)

# Eliminar el último elemento de la lista
lista.pop()
print("Lista después de eliminar el último elemento:", lista)

# Limpiar la lista
lista.clear()
print("Lista después de limpiar:", lista)

