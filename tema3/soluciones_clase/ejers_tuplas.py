# Ejercicios de tuplas

# Ejercicio 1
# Escribir una función que reciba una tupla de elementos e indique si se encuentran ordenados de menor a mayor o no. 

def ordenada(tupla: tuple) -> bool:
    if not isinstance(tupla, tuple):
        print("Error: la entrada no es una tupla")
        return None
    if len(tupla) == 0:
        print("La tupla está vacía")
        return True
    try:
        for i in range(len(tupla)-1):
            if tupla[i] > tupla[i+1]:
                return False
        return True
    except TypeError:
        print("Error: los elementos no son comparables")
        return None

# Pruebas
print(ordenada((1, 2, 3, 4, 5))) # True
print(ordenada((1, 2, 3, 5, 4))) # False
print(ordenada(())) # True, pero vamos a lanzar un mensaje avisando que la tupla está vacía
print(ordenada([1, 2, 3, 4, 5])) # None, vamos a lanzar un mensaje de que la entrada no es una tupla
print(ordenada(("a","b","c","d","e"))) # True
print(ordenada((1,"a"))) # None # Error
print(ordenada(345)) # None # Error

# Ejercicio 2
# Escribir una función que reciba una tupla de elementos e indique si se encuentran ordenados de mayor a menor o no.

def ordenada_inversa(tupla: tuple) -> bool:
    try:
        return ordenada(tupla[::-1])
    except TypeError:
        print("Error: debe ser un elemento iterable para poder recorrerlo")
        return None
    
# Pruebas
print(ordenada_inversa((5, 4, 3, 2, 1))) # True
print(ordenada_inversa((1, 2, 3, 4, 5))) # False
print(ordenada_inversa((1,"a"))) # False # Error
print(ordenada_inversa(345))

# Ejercicio 3
# Escribir una función que reciba una tupla de elementos e indique si son todos distintos o no. 

def distintos(tupla: tuple) -> bool:
    pass

# Pruebas
print(distintos((1, 2, 3, 4, 5))) # True
print(distintos((1, 2, 3, 4, 5, 1))) # False
print(distintos(())) # True

# Ejercicio 4
# Escribir una función que reciba una tupla de elementos e indique si es capicúa o no.  

def capicua(tupla: tuple) -> bool:
    pass

# Pruebas
print(capicua((1, 2, 3, 2, 1))) # True
print(capicua((1, 2, 3, 4, 5))) # False

# Ejercicio 5
# Escribir una función que reciba una tupla de números y un valor n y devuelva una lista con los elementos de la tupla que son múltiplos de n.

def multiplos(tupla: tuple, n: int) -> list:
    pass
    

# Pruebas
print(multiplos((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 2)) # [2, 4, 6, 8, 10]
print(multiplos((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 3)) # [3, 6, 9]

# Ejercicio 6
# Escribir una función que reciba una tupla de números y devuelva su máximo y su mínimo.    

def maximo_minimo(tupla: tuple) -> tuple:
    pass
    

# Pruebas
print(maximo_minimo((1, 2, 3, 4, 5))) # (5, 1)
print(maximo_minimo((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))) # (10, 1)
      
# Ejercicio 7
# Escribir una función que reciba una tupla de números y devuelva su media y su varianza.   

def media_varianza(tupla: tuple) -> tuple:
    pass

# Pruebas
print(media_varianza((1, 2, 3, 4, 5))) # (3.0, 2.0)
print(media_varianza((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))) # (5.5, 8.25)
      
# Ejercicio 8
# Escribir una función que reciba una tupla de números y devuelva la tupla con sus elementos ordenados de menor a mayor.

def ordenar_tupla(tupla: tuple) -> tuple:
    pass

# Pruebas
print(ordenar_tupla((5, 4, 3, 2, 1))) # (1, 2, 3, 4, 5)
print(ordenar_tupla((1, 2, 3, 5, 4))) # (1, 2, 3, 4, 5)