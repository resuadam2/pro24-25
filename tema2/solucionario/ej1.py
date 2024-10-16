# Ejercicio 1
"""
Disear una función que intercambie el valor de dos variables de tipo entero. 
Incluir el algoritmo principal que realice la llamada a dicha función.
"""

def intercambiar(a, b):
    aux = a
    a = b
    b = aux
    return a, b

if __name__ == "__main__":
    a = 5
    b = 10
    print(f"Antes de intercambiar: a = {a}, b = {b}")
    a, b = intercambiar(a, b)
    print(f"Después de intercambiar: a = {a}, b = {b}")
