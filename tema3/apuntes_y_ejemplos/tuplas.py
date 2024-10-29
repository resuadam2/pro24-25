# Tuplas en Python

# Las tuplas son una estructura de datos similar a las listas, pero con la diferencia de que son inmutables, 
# es decir, no se pueden modificar una vez creadas. 
# Se crean con paréntesis y los elementos se separan por comas.
# Las tuplas son más rápidas que las listas y ocupan menos espacio en memoria.
# Se pueden acceder a los elementos de una tupla mediante su índice, igual que en las listas.
# Las tuplas pueden contener elementos de diferentes tipos.
# Las tuplas pueden contener otras tuplas.
# Las tuplas pueden contener listas.
# Las tuplas pueden contener diccionarios.
# Las tuplas pueden contener conjuntos.
# Las tuplas pueden contener cualquier combinación de los tipos de datos anteriores.
# Las tuplas pueden contener elementos duplicados.
# Las tuplas pueden contener elementos nulos.
# Las tuplas pueden contener elementos vacíos.

# Crear una tupla vacía
tupla_vacia = ()
print(tupla_vacia)

# Crear una tupla con un solo elemento
tupla_un_elemento = (1,)
print(tupla_un_elemento)

# Otra forma de crear una tupla con un solo elemento
tupla_un_elemento = 1, # Sin paréntesis, pero la coma es necesaria, sin ella se crea una variable de tipo entero
print(tupla_un_elemento)

# Crear una tupla con varios elementos
tupla = (1, 2, 3, 4, 5)
print(tupla)

# Crear una tupla con elementos de diferentes tipos
tupla_tipos = (1, 'hola', 3.14, True)
print(tupla_tipos)

# Crear una tupla con tuplas
tupla_tuplas = ((1, 2), (3, 4), (5, 6))
print(tupla_tuplas)

# Crear una tupla con listas
tupla_listas = ([1, 2], [3, 4], [5, 6])
print(tupla_listas)

# Crear una tupla con diccionarios
tupla_diccionarios = ({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})
print(tupla_diccionarios)

# Crear una tupla con conjuntos
tupla_conjuntos = ({1, 2}, {3, 4}, {5, 6})
print(tupla_conjuntos)

# Acceso a los elementos de una tupla
tupla = (1, 2, 3, 4, 5)

# Acceder al primer elemento
print(tupla[0])

# Acceder al último elemento
print(tupla[-1])

# Acceder a un rango de elementos
print(tupla[1:4])

# Acceder a un rango de elementos con saltos
print(tupla[0:5:2])

# Acceder a un rango de elementos con saltos negativos
print(tupla[5:0:-2])

# Las tuplas son inmutables, no se pueden modificar
tupla = (1, 2, 3, 4, 5)

# Intentar modificar un elemento de la tupla
try:
    tupla[0] = 10
except TypeError as e:
    print(e)

# Intentar añadir un elemento a la tupla
try:
    tupla.append(6)
except AttributeError as e:
    print(e)

# Intentar eliminar un elemento de la tupla
try:
    del tupla[0]
except TypeError as e:
    print(e)

# Intentar eliminar la tupla - Se elimina la tupla, no los elementos, la tupla entera
try:
    del tupla
except AttributeError as e:
    print(e)

try:
    print(tupla)
except NameError as e:
    print(e) # name 'tupla' is not defined, por lo tanto, la tupla ha sido eliminada

# Operaciones con tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

# Concatenar tuplas
tupla3 = tupla1 + tupla2
print(tupla3)

# Multiplicar tuplas
tupla4 = tupla1 * 3
print(tupla4)

# Longitud de una tupla
print(len(tupla1))

# Comprobar si un elemento está en la tupla
print(1 in tupla1)

# Comprobar si un elemento no está en la tupla
print(1 not in tupla1)

# Iterar sobre una tupla
for elemento in tupla1:
    print(elemento)

# Desempaquetar una tupla
tupla = (1, 2, 3)
a, b, c = tupla
print(a, b, c)

# Desempaquetar una tupla con un asterisco
tupla = (1, 2, 3, 4, 5)
a, b, *c = tupla
print(a, b, c) # c es una lista

# Convertir una lista en una tupla usando la función tuple()
lista = [1, 2, 3, 4, 5]
tupla = tuple(lista)
print(tupla)

# Convertir una tupla en una lista usando la función list()
tupla = (1, 2, 3, 4, 5)
lista = list(tupla)
print(lista)

# Convertir una cadena en una tupla
cadena = 'hola'
tupla = tuple(cadena)
print(tupla)

# Convertir una tupla en una cadena
tupla = ('h', 'o', 'l', 'a')
cadena = ''.join(tupla)
print(cadena)
