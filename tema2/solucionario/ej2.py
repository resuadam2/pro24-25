# Ejercicio 2

"""
Diseñar una función que tenga como entrada tres números enteros y nos devuelva el mayor de los tres.
Incluir el algoritmo principal que realice la llamada a dicha función.
"""

def mayor_de_tres(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    
if __name__ == "__main__":
    a = 5
    b = 10
    c = 3
    print(f"El mayor de los tres números es: {mayor_de_tres(a, b, c)}")
