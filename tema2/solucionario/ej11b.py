# Ejercicio 11 - Sin usar funciones de las listas

"""
Diseñar una función que determine la posición del valor máximo de una lista de enteros
y otra para indicar cuál es ese valor máximo.
Incluir un programa que pruebe ambas funciones.
"""

def posicion_maximo(lista):
    maximo = lista[0]
    posicion = 0
    for i in range(1, len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
            posicion = i
    return posicion

def valor_maximo(lista):
    maximo = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
    return maximo

if __name__ == "__main__":
    lista = [4, 6, 7, 2, 3, 8, 5]
    print(f"La posición del valor máximo de la lista {lista} es: {posicion_maximo(lista)}")
    print(f"El valor máximo de la lista {lista} es: {valor_maximo(lista)}")

# Output
# La posición del valor máximo de la lista [4, 6, 7, 2, 3, 8, 5] es: 5
# El valor máximo de la lista [4, 6, 7, 2, 3, 8, 5] es: 8
