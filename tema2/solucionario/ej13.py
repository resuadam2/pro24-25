# Ejercicio 13

"""
Diseñar una función para sumar dos matrices bidimensionales de enteros.
Las matrices se representarán como listas de listas y deben pasarse como argumentos a las funciones.    
Incluir un programa que pruebe ambas funciones.
"""

def sumar_matrices(matriz1, matriz2):
    suma = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz1[i])):
            fila.append(matriz1[i][j] + matriz2[i][j])
        suma.append(fila)
    return suma

if __name__ == "__main__":
    matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matriz2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    print(f"La suma de las matrices {matriz1} y {matriz2} es: {sumar_matrices(matriz1, matriz2)}")