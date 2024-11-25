# Ejercicios sobre control de excepciones

# Ejercicio 1

# Escribir una función que reciba dos números y devuelva su división. Si el segundo número es cero debe devolver un mensaje de error.   

def division(a: float, b: float) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: División por cero")
        return None
    except TypeError:
        print("Error: Los argumentos deben ser números")
        return None
    except:
        print("Error")
        return
    
# Pruebas
print(division(4, 2)) # 2.0
print(division(4, 0)) # Error: División por cero
print(division("a", 2)) # Error: Los argumentos deben ser números

# Ejercicio 2

# Escribir una función que reciba una lista de números y devuelva su media. Si la lista está vacía debe devolver un mensaje de error.

def media(lista: list) -> float:
    try:
        return sum(lista) / len(lista)
    except ZeroDivisionError:
        print("Error: Lista vacía")
        return None
    except TypeError:
        print("Error: Los elementos de la lista deben ser números")
        return None
    except:
        print("Error")
        return  
    
# Pruebas
print(media([1, 2, 3, 4, 5])) # 3.0
print(media([])) # Error: Lista vacía
print(media([1, "a", 3, 4, 5])) # Error: Los elementos de la lista deben ser números

# Ejercicio 3

# Escribir una función que reciba una cadena y un número n y devuelva la cadena repetida n veces. Si el número es negativo debe devolver un mensaje de error.   

def repetir(cadena: str, n: int) -> str:
    try:
        return cadena * n
    except TypeError:
        print("Error: El segundo argumento debe ser un número")
        return ""
    except:
        print("Error")
        return ""
    
# Pruebas
print(repetir("hola", 3)) # holaholahola
print(repetir("adiós", -2)) # Error: El segundo argumento debe ser un número
print(repetir(2, 3)) # Error

# Ejercicio 4

# Escribir una función que reciba una lista de números y devuelva una lista con los cuadrados de los números. Si la lista contiene algún elemento que no es un número debe devolver un mensaje de error.    

def cuadrados(lista: list) -> list:
    try:
        return [x ** 2 for x in lista]
    except TypeError:
        print("Error: Los elementos de la lista deben ser números")
        return []
    except:
        print("Error")
        return []   
    
# Pruebas
print(cuadrados([1, 2, 3, 4, 5])) # [1, 4, 9, 16, 25]
print(cuadrados([1, "a", 3, 4, 5])) # Error: Los elementos de la lista deben ser números
print(cuadrados([])) # []

# Ejercicio 5

# Escribir una función que reciba una tupla y una posición y devuelva el elemento de la tupla en la posición indicada. Si la posición es mayor que la longitud de la tupla debe devolver un mensaje de error.

def elemento(tupla: tuple, pos: int):
    try:
        return tupla[pos]
    except IndexError:
        print("Error: La posición no existe")
        return None
    except TypeError:
        print("Error: El segundo argumento debe ser un número")
        return None
    except:
        print("Error")
        return  
    
# Pruebas
print(elemento((1, 2, 3, 4, 5), 2)) # 3
print(elemento((1, 2, 3, 4, 5), 5)) # Error: La posición no existe
print(elemento((1, 2, 3, 4, 5), "a")) # Error: El segundo argumento debe ser un

# Ejercicio 6

# Escribir una función que reciba un diccionario y una clave y devuelva el valor asociado a la clave. Si la clave no existe debe devolver un mensaje de error.  

def valor(diccionario: dict, clave: str):
    try:
        if not isinstance(diccionario, dict):
            raise TypeError
        return diccionario[clave]
    except KeyError:
        print("Error: La clave no existe")
        return None
    except TypeError:
        print("Error: Debe introducir un diccionario")
        return None
    except:
        print("Error")
        return  
    
# Pruebas
print(valor({"a": 1, "b": 2, "c": 3}, "b")) # 2
print(valor({"a": 1, "b": 2, "c": 3}, "d")) # Error: La clave no existe
print(valor({"a": 1, "b": 2, "c": 3, 2: 4}, 2)) # 4
print(valor([1, 2, 3], 2)) # Error de tipo

# Ejercicio 7

# Escribir una función que reciba una lista de números y devuelva el número más grande. Si la lista está vacía debe devolver un mensaje de error.   

def maximo(lista: list) -> float:
    try:
        return max(lista)
    except ValueError:
        print("Error: Lista vacía")
        return None
    except TypeError:
        print("Error: Los elementos de la lista deben ser números")
        return None
    except:
        print("Error")
        return  
    
# Pruebas
print(maximo([1, 2, 3, 4, 5])) # 5
print(maximo([])) # Error: Lista vacía
print(maximo([1, "a", 3, 4, 5])) # Error: Los elementos de la lista deben ser números   


