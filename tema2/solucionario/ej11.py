# Ejercicio 11

"""
Diseñar una función que determine la posición del valor máximo de una lista de enteros
y otra para indicar cuál es ese valor máximo.
Incluir un programa que pruebe ambas funciones.
"""

def posicion_maximo(lista):
    return lista.index(max(lista))

def valor_maximo(lista):
    return max(lista)

if __name__ == "__main__":
    lista = [4, 6, 7, 2, 3, 8, 5]
    print(f"La posición del valor máximo de la lista {lista} es: {posicion_maximo(lista)}")
    print(f"El valor máximo de la lista {lista} es: {valor_maximo(lista)}")

# Output
# La posición del valor máximo de la lista [4, 6, 7, 2, 3, 8, 5] es: 5
# El valor máximo de la lista [4, 6, 7, 2, 3, 8, 5] es: 8