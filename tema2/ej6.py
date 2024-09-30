# Ejercicio 6

"""
Diseñar una función que decida si dos números enteros positivos son amigos.
Dos números son amigos si la suma de los divisores propios de uno es igual al otro número y viceversa.
Por ejemplo, los divisores propios de 220 son 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 y 110, que suman 284.
Los divisores propios de 284 son 1, 2, 4, 71 y 142, que suman 220.
Incluir el algoritmo principal que realice la llamada a dicha función.
"""

def divisores_propios(numero):
    divisores = []
    for i in range(1, numero):
        if numero % i == 0:
            divisores.append(i)
    return divisores

def son_amigos(a, b):
    if sum(divisores_propios(a)) == b and sum(divisores_propios(b)) == a:
        return True
    else:
        return False
    
if __name__ == "__main__":
    a = 220
    b = 284
    if son_amigos(a, b):
        print(f"Los números {a} y {b} son amigos.")
    else:
        print(f"Los números {a} y {b} no son amigos.")
    
    a = 1184
    b = 1210
    if son_amigos(a, b):
        print(f"Los números {a} y {b} son amigos.")
    else:
        print(f"Los números {a} y {b} no son amigos.")

    a = 220
    b = 1210
    if son_amigos(a, b):
        print(f"Los números {a} y {b} son amigos.")
    else:
        print(f"Los números {a} y {b} no son amigos.")
