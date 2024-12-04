# Ejercicios con conjuntos

# Ejercicio 1

# Escribir una función que reciba dos conjuntos y devuelva un conjunto con los elementos que están en ambos conjuntos.

def interseccion(conjunto1: set, conjunto2: set) -> set:
    try:
        return conjunto1.intersection(conjunto2)
    except AttributeError:
        print("Por favor, introduzca dos conjuntos")
    except:
        print("Error inesperado")

    
# Pruebas
print(interseccion({1, 2, 3}, {3, 4, 5})) # {3}
print(interseccion({1, 2, 3}, {4, 5, 6})) # set() ya que no tienen elementos en común   
print(interseccion(4,5))
print(interseccion({},[1,2,3,4,5]))

# Ejercicio 2

# Escribir una función que reciba dos conjuntos y devuelva un conjunto con los elementos que están en el primer conjunto pero no en el segundo. 

def diferencia(conjunto1: set, conjunto2: set) -> set:
    try:
        return conjunto1.difference(conjunto2)
    except AttributeError:
        print("Por favor, introduzca dos conjuntos")
    except:
        print("Error inesperado")    
    
# Pruebas
print(diferencia({1, 2, 3}, {3, 4, 5})) # {1, 2}
print(diferencia({1, 2, 3}, {4, 5, 6})) # {1, 2, 3} ya que el primer conjunto no tiene elementos en el segundo  

# Ejercicio 3

# Escribir una función que reciba dos conjuntos y devuelva un conjunto con los elementos que están en alguno de los dos conjuntos pero no en los dos. 

def diferencia_simetrica(conjunto1: set, conjunto2: set) -> set:
    try:
        return conjunto1.symmetric_difference(conjunto2)
    except AttributeError:
        print("Por favor, introduzca dos conjuntos")
    except:
        print("Error inesperado")   
    
# Pruebas
print(diferencia_simetrica({1, 2, 3}, {3, 4, 5})) # {1, 2, 4, 5}
print(diferencia_simetrica({1, 2, 3}, {4, 5, 6})) # {1, 2, 3, 4, 5, 6} ya que no tienen elementos en común

# Ejercicio 4

# Escribir una función que reciba una lista de enteros y devuelva otra lista sin elementos repetidos, para ello se puede convertir la lista en un conjunto y después volver a convertirlo en lista. 

def eliminar_repetidos(lista: list) -> list:
    try:
        return list(set(lista))
    except TypeError:
        print("Por favor, introduzca una lista")
    
# Pruebas
print(eliminar_repetidos([1, 2, 3, 3, 4, 5, 5])) # [1, 2, 3, 4, 5]
print(eliminar_repetidos([1, 2, 3, 4, 5])) # [1, 2, 3, 4, 5] ya que no hay elementos repetidos  
print(eliminar_repetidos(1234))
print(eliminar_repetidos([]))
print(eliminar_repetidos({2:2,3:3,4:4,3:3}))

# Ejercicio 5

# Escribir una función que reciba una lista de palabras y devuelva un conjunto con las palabras que tienen más de n caracteres. 

def palabras_mas_de_n_caracteres(lista: list, n: int) -> set:
    try:
        toret = set()
        for palabra in lista:
            if len(palabra) > n:
                toret.add(palabra)
        return toret    
    except TypeError:
        print("N debe de ser un valor entero")
    except:
        print("Ha ocurrido un error inesperado")

def palabras_mas_de_n_caracteres(lista: list, n: int) -> set:
    try:
        return {palabra for palabra in lista if len(palabra) > n}
    except TypeError:
        print("N debe de ser un valor entero")
    except:
        print("Ha ocurrido un error inesperado")
    
# Pruebas
print(palabras_mas_de_n_caracteres(["hola", "mundo", "python", "adiós"], 4)) # {"mundo","python", "adiós"}  
print(palabras_mas_de_n_caracteres(["hola", "mundo", "python", "adiós"], 5)) # {"python"} ya que solo hay una palabra con más de 5 caracteres   
print(palabras_mas_de_n_caracteres(["python", "python", "python","hola"], 4)) # {"python"}
print(palabras_mas_de_n_caracteres([], 3)) # {}
print(palabras_mas_de_n_caracteres("asdf", 4)) # {}
print(palabras_mas_de_n_caracteres(["python", "python", "python","hola"], "asdf")) # {"python"}
print(palabras_mas_de_n_caracteres([""], 0))


# Ejercicio 6

# Escribir una función que dadas dos palabras devuelva un conjunto con las letras que tienen en común.

def letras_en_comun(palabra1: str, palabra2: str) -> set:
    try:
        return set(palabra1).intersection(palabra2)
    except AttributeError:
        print("Por favor, introduzca dos strings")
    except TypeError:
        print("Por favor, introduzca dos strings")
    except:
        print("Error inesperado")

    
# Pruebas
print(letras_en_comun("hola", "adiós")) # {"a"}
print(letras_en_comun("hola", "mundo")) # {"o"} ya que es la única letra que tienen en común
print(letras_en_comun(1234, 1234))

# Ejercicio 7

# Escribir una función que reciba dos listas y nos diga si la primera lista está contenida en la segunda o no, utiliza operadores de conjuntos para ello.

def lista_contenida(lista1: list, lista2: list) -> bool:
    try:
        return set(lista1).issubset(lista2)
    except TypeError:
        print("Debes pasar un elemento iterable")
    except:
        print("Error inesperado")
    
# Pruebas
print(lista_contenida([1, 2], [1, 2, 3, 4])) # True
print(lista_contenida([1, 2, 3], [1, 2])) # False ya que la primera lista no está contenida en la segunda
print(lista_contenida(2134, 2134))
print(lista_contenida([], []))
print(lista_contenida("adsf", "qwer"))
