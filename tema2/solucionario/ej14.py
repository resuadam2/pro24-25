# Ejercicio 14

"""
En el ejercicio anterior ya viste que visualizar las listas como matrices simplemente
imprimiendolas con print no es suficiente. Diseña una función que imprima una matriz
bidimensional de enteros de manera que se vea como una matriz (no es necesario incluir 
 los paréntesis grandes, tan solo separar los números con tabulaciones y saltos de línea). 
Incluir un programa que pruebe la función.
"""

def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end="\t")
        print()

if __name__ == "__main__":
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    imprimir_matriz(matriz)