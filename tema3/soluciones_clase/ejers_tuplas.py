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
    try:
        if not isinstance(tupla, tuple):
            raise TypeError
        for i in range(len(tupla)):
            for j in range(i+1, len(tupla)):
                if tupla[i] == tupla[j]:
                    return False
        return True
    except TypeError:
        print("Error: esta función solo admite tuplas")
        return None
    except:
        print("Error inesperado")
        return None

# Pruebas
print(distintos((1, 2, 3, 4, 5))) # True
print(distintos((1, 2, 3, 4, 5, 1))) # False
print(distintos(())) # True
print(distintos(4)) # None # Error
print(distintos([1, 2, 3, 4, 5])) # None # Error

# Ejercicio 4
# Escribir una función que reciba una tupla de elementos e indique si es capicúa o no.  

def capicua(tupla: tuple) -> bool:
    try:
        if not isinstance(tupla, tuple):
            raise TypeError
        return tupla == tupla[::-1]
    except TypeError:
        print("Error: esta función solo admite tuplas")
        return None
    
def capicua_v2(tupla: tuple) -> bool:
    try:
        if not isinstance(tupla, tuple):
            raise TypeError
        for i in range(len(tupla)//2):
            if tupla[i] != tupla[-i-1]:
                return False
        return True
    except TypeError:
        print("Error: esta función solo admite tuplas")
        return None

# Pruebas
print(capicua((1, 2, 3, 2, 1))) # True
print(capicua((1, 2, 3, 4, 5))) # False
print(capicua(1234)) # None # Error
print(capicua([1, 2, 3, 2, 1])) # None # Error

print(capicua_v2((1, 2, 3, 2, 1))) # True
print(capicua_v2((1, 2, 3, 4, 5))) # False
print(capicua_v2(1234)) # None # Error
print(capicua_v2([1, 2, 3, 2, 1])) # None # Error

# Ejercicio 5
# Escribir una función que reciba una tupla de números y un valor n y devuelva una lista con los elementos de la tupla que son múltiplos de n.

def multiplos(tupla: tuple, n: int) -> list:
    try:
        return [i for i in tupla if i % n == 0]
    except ZeroDivisionError:
        print("Error: el divisor no puede ser 0")
    except TypeError:
        print("Error: la tupla debe contener solo números")
    except:
        print("Error inesperado")
    

# Pruebas
print(multiplos((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 2)) # [2, 4, 6, 8, 10]
print(multiplos((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 3)) # [3, 6, 9]
print(multiplos((1, 2, 3, 4, 5, 6, "H", 8, 9, 10), 5)) # Error
print(multiplos((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), "H")) # Error
print(multiplos((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 0)) # [0]
print(multiplos((), 4))
print(multiplos(4, 2)) # Error

# Ejercicio 6
# Escribir una función que reciba una tupla de números y devuelva su máximo y su mínimo.    

def maximo_minimo(tupla: tuple) -> tuple:
    try:
        return (max(tupla), min(tupla))
    except ValueError:
        print("Error: la tupla está vacía")
    except TypeError:
        print("Error: la tupla debe contener solo números")
    except:
        print("Error inesperado")
    

# Pruebas
print(maximo_minimo((1, 2, 3, 4, 5))) # (5, 1)
print(maximo_minimo((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))) # (10, 1)
print(maximo_minimo(())) # Error
      
# Ejercicio 7
# Escribir una función que reciba una tupla de números y devuelva su media y su varianza.   

def media_varianza(tupla: tuple) -> tuple:
    try:
        media = sum(tupla) / len(tupla)
        varianza = sum((x - media)**2 for x in tupla) / len(tupla)
        return (media, varianza)
    except ZeroDivisionError:
        print("Error: la tupla está vacía")
    except TypeError:
        print("Error: la tupla debe contener solo números")
    except:
        print("Error inesperado")

# Pruebas
print(media_varianza((1, 2, 3, 4, 5))) # (3.0, 2.0)
print(media_varianza((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))) # (5.5, 8.25)
print(media_varianza(())) # (0.0, 0.0)
print(media_varianza((1, 2, 3, 4, 5, 6, "H", 8, 9, 10))) # Error
print(media_varianza(1234)) # Error
print(media_varianza([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])) # (6.0, 10.0)
      
# Ejercicio 8
# Escribir una función que reciba una tupla de números y devuelva la tupla con sus elementos ordenados de menor a mayor.

def ordenar_tupla(tupla: tuple) -> tuple:
    try:
        return tuple(sorted(tupla))
    except TypeError:
        print("Error: la tupla debe contener solo números")
    except:
        print("Error inesperado")

def ordenar_tupla_v2(tupla: tuple) -> tuple:
    try:
        lista = list(tupla)
        lista.sort()
        return tuple(lista)
    except TypeError:
        print("Error: la tupla debe contener solo números")
    except:
        print("Error inesperado")

def ordenar_tupla_v3(tupla: tuple) -> tuple:
    try:
        lista = list(tupla)
        for i in range(len(lista)):
            for j in range(i+1, len(lista)):
                if lista[i] > lista[j]:
                    lista[i], lista[j] = lista[j], lista[i]
        return tuple(lista)
    except TypeError:
        print("Error: la tupla debe contener solo números")
    except:
        print("Error inesperado")

# Pruebas
print(ordenar_tupla((5, 4, 3, 2, 1))) # (1, 2, 3, 4, 5)
print(ordenar_tupla((1, 2, 3, 5, 4))) # (1, 2, 3, 4, 5)
print(ordenar_tupla(())) # ()
print(ordenar_tupla(1234)) # Error
print(ordenar_tupla([1, 2, 3, 4, 5])) # Si quisieramos controlar el que no reciba listas, habría que usar isinstance
print(ordenar_tupla(("c","b","a","d","e"))) # ("a", "b", "c", "d", "e")