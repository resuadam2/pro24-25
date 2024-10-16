# Ejercicio 7

"""
Diseñar una función que dado un número entero positivo, diga si es o no un número perfecto.
Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos.
Por ejemplo, 6 es perfecto porque sus divisores propios son 1, 2 y 3, que suman 6.
Incluir el algoritmo principal que realice la llamada a dicha función.
"""

def divisores_propios(numero):
    divisores = []
    for i in range(1, numero):
        if numero % i == 0:
            divisores.append(i)
    return divisores

def es_perfecto(numero):
    if sum(divisores_propios(numero)) == numero:
        return True
    else:
        return False
    
if __name__ == "__main__":
    numero = 6
    if es_perfecto(numero):
        print(f"El número {numero} es perfecto.")
    else:
        print(f"El número {numero} no es perfecto.")
    
    numero = 28
    if es_perfecto(numero):
        print(f"El número {numero} es perfecto.")
    else:
        print(f"El número {numero} no es perfecto.")

    numero = 496
    if es_perfecto(numero):
        print(f"El número {numero} es perfecto.")
    else:
        print(f"El número {numero} no es perfecto.")

    numero = 8128
    if es_perfecto(numero):
        print(f"El número {numero} es perfecto.")
    else:
        print(f"El número {numero} no es perfecto.")

    numero = 12
    if es_perfecto(numero):
        print(f"El número {numero} es perfecto.")
    else:
        print(f"El número {numero} no es perfecto.")
