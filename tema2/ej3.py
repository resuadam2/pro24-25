# Ejercicio 3

"""
Diseñar una función que permita calcular el número e, o número de Euler, mediante la siguiente serie infinita:
e = 1 + 1/1! + 1/2! + 1/3! + 1/4! + ...
para una precisión dada por el usuario, la precisión indicará las vueltas que debe dar el algoritmo a la 
serie infinita. Incluir el algoritmo principal que realice la llamada a dicha función.
Como paso previo, se puede diseñar una función que calcule el factorial de un número entero.
"""

import math

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1) # Recursividad para calcular el factorial de un número
    
def euler(precision):
    e = 1
    n = 1
    while n < precision:
        e += 1 / factorial(n)
        n += 1
    return e

if __name__ == "__main__":
    precision = float(input("Introduce la precisión deseada: "))
    print(f"El número e con una precisión de {precision} es: {euler(precision)}")

    print("El número de euler calculado por la función math es: ", math.e) # Comprobación con la función math de Python

