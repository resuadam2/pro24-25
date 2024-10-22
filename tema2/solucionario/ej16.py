# Ejercicio 16

"""
Diseñar una función que nos compruebe si una matriz bidimensional de enteros es simétrica.
Las matrices se representarán como listas de listas y deben pasarse como argumentos a las funciones.
Una matriz es simétrica si es cuadrada y es igual a su traspuesta.
La traspuesta de una matriz se obtiene intercambiando filas por columnas.
Incluir más funciones si es necesario.
Incluir un programa que pruebe la función.
"""

def traspuesta(matriz):
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

def es_simetrica(matriz):
    if len(matriz) != len(matriz[0]):
        return False
    return matriz == traspuesta(matriz)

def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end="\t")
        print()

if __name__ == "__main__":
    matriz = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
    print(f"La matriz {matriz} es simétrica: {es_simetrica(matriz)}")
    print("Matriz:")
    imprimir_matriz(matriz)

