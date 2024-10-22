# Ejercicio 12 - Sin usar slicing

"""
Diseñar una función que devuelva una lista invertida a partir de otra.
Incluir un programa que pruebe la función.
"""

def invertir_lista(lista):
    invertida = []
    for i in range(len(lista) - 1, -1, -1):
        invertida.append(lista[i])
    return invertida


if __name__ == "__main__":
    lista = [4, 6, 7, 2, 3, 8, 5]
    print(f"La lista invertida de {lista} es: {invertir_lista(lista)}")