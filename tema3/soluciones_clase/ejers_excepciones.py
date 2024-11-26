# Ejercicios sobre control de excepciones

# Ejercicio 1

# Escribir una función que reciba dos números y devuelva su división. Si el segundo número es cero debe devolver un mensaje de error.   

def division(a: float, b: float) -> float:
    """
    Función que recibe dos números y devuelve su división.
    Parámetros:
        a: Es un número flotante.
        b: Es un número flotante distinto de cero.
        
        Devuelve:
        La división de a entre b.
        None si b es cero o no es un número.
    """
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: División por cero")
        return None
    except TypeError:
        print("Error: Los argumentos deben ser números")
        return None
    except:
        print("Error inesperado")
        return None

# Pruebas
resultado = division(4, 2) # 2.0
print(resultado)
resultado = division(4, 0) # Error: División por cero
print(resultado)
resultado = division("a", 2) # Error: Los argumentos deben ser números
print(resultado)

# Ejercicio 2

# Escribir una función que reciba una lista de números y devuelva su media. Si la lista está vacía debe devolver un mensaje de error.

def media(lista: list) -> float:
    try:
        if(isinstance(lista, list) == False):
            raise TypeError
        return sum(lista) / len(lista)
    except ZeroDivisionError:
        print("Error: Lista vacía")
        return None
    except TypeError:
        print("Error: Los elementos de la lista deben ser números y la lista debe ser una lista")
        return None
    except Exception: # Captura cualquier otra excepción no controlada, es lo mismo que "except:"
        print("Error inesperado")
        return None
    
# Pruebas
print(media([1, 2, 3, 4, 5])) # 3.0
print(media((1, 2, 3, 4, 5))) # Error: Los elementos de la lista deben ser números
print(media([])) # Error: Lista vacía
print(media([1, "a", 3, 4, 5])) # Error: Los elementos de la lista deben ser números

# Ejercicio 3

# Escribir una función que reciba una cadena y un número n y devuelva la cadena repetida n veces. Si el número es negativo debe devolver un mensaje de error.   

def repetir(cadena: str, n: int) -> str:
    try:
        if n < 0:
            raise ValueError
        return str(cadena) * n
    except ValueError:
        print("Error: El segundo argumento debe ser un número positivo")
    except TypeError:
        print("Error: El segundo argumento debe ser un número")
    except:
        print("Error inesperado")

    
    
    
# Pruebas
print(repetir("hola", 3)) # holaholahola
print(repetir("adiós", -2)) # Error: El segundo argumento debe ser un número positivo
print(repetir(2, 3))
print(repetir("hola", "3")) # Error: El segundo argumento debe ser un número
print(repetir([2,3,4], 3)) 
print(repetir("hola", 0)) # ""

# Ejercicio 4

# Escribir una función que reciba una lista de números y devuelva una lista con los cuadrados de los números. Si la lista contiene algún elemento que no es un número debe devolver un mensaje de error.    

def cuadrados(lista: list) -> list:
    try:
        return [i ** 2 for i in lista]
    except TypeError:
        print("Error: Los elementos de la lista deben ser números")
        return None
    except:
        print("Error inesperado")
        return None
    
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
    except TypeError:
        print("Error: El segundo argumento debe ser un número")
    except:
        print("Error inesperado")
    
# Pruebas
print(elemento((1, 2, 3, 4, 5), 2)) # 3
print(elemento((1, 2, 3, 4, 5), 5)) # Error: La posición no existe
print(elemento((1, 2, 3, 4, 5), "a")) # Error: El segundo argumento debe ser un

# Ejercicio 6

# Escribir una función que reciba un diccionario y una clave y devuelva el valor asociado a la clave. 
# Si la clave no existe debe devolver un mensaje de error.  

def valor(diccionario: dict, clave: str):
    try:
        if not isinstance(diccionario, dict):
            raise TypeError("Error: el primer parámetro debe ser un diccionario")
        if not isinstance(clave, str):
            raise TypeError("Error: el segundo parámetro debe ser una string")
        return diccionario[clave]
    except KeyError:
        print("Error: La clave no existe")
    except TypeError as e:
        print(e)
    except:
        print("Error inesperado")
    
# Pruebas
print(valor({"a": 1, "b": 2, "c": 3}, "b")) # 2
print(valor({"a": 1, "b": 2, "c": 3}, "d")) # Error: La clave no existe
print(valor([1,2,3,4], 2)) # Error: el primer parámetro debe ser un diccionario
print(valor({"a": 1, 2: 2, "c": 3}, 2)) # 2
print(valor({"a": 1, 2: 2, "c": 3}, ["a"])) # 1

# Ejercicio 7

# Escribir una función que reciba una lista de números y devuelva el número más grande. Si la lista está vacía debe devolver un mensaje de error.   

def maximo(lista: list) -> float:
    try:
        return max(lista)
    except ValueError:
        print("Error: Lista vacía")
        return None
    except TypeError:
        print("Error: Debe ser una lista de números")
        return None
    except:
        print("Error inesperado")
        return None
    
# Pruebas
print(maximo([1, 2, 3, 4, 5])) # 5
print(maximo(["a","B"])) 
print(maximo([[3,3],[1,4]])) # [3, 3]
print(maximo(2134)) # Error: Los elementos de la lista deben ser números
print(maximo([])) # Error: Lista vacía
print(maximo([1, "a", 3, 4, 5])) # Error: Los elementos de la lista deben ser números   


