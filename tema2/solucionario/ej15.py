# Ejercicio 15

"""
Diseñar una función para multiplicar dos matrices bidimensionales de enteros.
Las matrices se representarán como listas de listas y deben pasarse como argumentos a las funciones.
Para multiplicar dos matrices, el número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.   
La multiplicación de matrices se calcula multiplicando cada elemento de la fila de la primera matriz por cada elemento de la columna de la segunda matriz y sumando los resultados. 
Incluir un programa que pruebe la función.

Nota: Puedes usar la función del ejercicio 14 para visualizar mejor las matrices
"""

def multiplicar_matrices(matriz1, matriz2):
    if len(matriz1[0]) != len(matriz2):
        return None
    producto = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz2[0])):
            suma = 0
            for k in range(len(matriz1[i])):
                suma += matriz1[i][k] * matriz2[k][j]
            fila.append(suma)
        producto.append(fila)
    return producto

def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end="\t")
        print()

if __name__ == "__main__":
    matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matriz2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    producto = multiplicar_matrices(matriz1, matriz2)

    if producto:
        print("Matriz 1:")
        imprimir_matriz(matriz1)
        print("Matriz 2:")
        imprimir_matriz(matriz2)
        print("Producto:")
        imprimir_matriz(producto)
