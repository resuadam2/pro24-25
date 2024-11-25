# Diccionarios en Python

# Los diccionarios son una estructura de datos que permite almacenar pares clave-valor.
# Se crean con llaves y los elementos se separan por comas.
# Los diccionarios son mutables, es decir, se pueden modificar una vez creados.
# Los diccionarios no permiten claves duplicadas.
# Los diccionarios no permiten claves nulas.
# Los diccionarios no permiten claves vacías.
# Los diccionarios permiten valores duplicados.
# Los diccionarios permiten valores nulos.
# Los diccionarios permiten valores vacíos.
# Los diccionarios pueden contener cualquier tipo de dato.
# Los diccionarios pueden contener diccionarios.
# Los diccionarios pueden contener listas.
# Los diccionarios pueden contener tuplas.
# Los diccionarios pueden contener conjuntos.
# Los diccionarios pueden contener cualquier combinación de los tipos de datos anteriores.

# Crear un diccionario vacío
diccionario_vacio = {}
print(diccionario_vacio)

# Crear un diccionario con un solo elemento
diccionario_un_elemento = {'a': 1}
print(diccionario_un_elemento)

# Crear un diccionario con varios elementos
diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(diccionario)

# Crear un diccionario con claves de diferentes tipos
diccionario_tipos = {1: 'uno', 'dos': 2, 3.0: 'tres', True: 'cuatro', False: 'cinco', 0: 'seis'}
print(diccionario_tipos)

# Crear un diccionario con diccionarios
diccionario_diccionarios = {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': 4}, 'g': {'h': 5, 'i': 6}}
print(diccionario_diccionarios)

# Crear un diccionario con listas
diccionario_listas = {'a': [1, 2], 'b': [3, 4], 'c': [5, 6]}
print(diccionario_listas)

# Crear un diccionario con tuplas
diccionario_tuplas = {'a': (1, 2), 'b': (3, 4), 'c': (5, 6)}
print(diccionario_tuplas)

# Crear un diccionario con conjuntos
diccionario_conjuntos = {'a': {1, 2}, 'b': {3, 4}, 'c': {5, 6}}
print(diccionario_conjuntos)

# Acceso a los elementos de un diccionario
diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Acceder al valor de una clave
print(diccionario['a'])

# Modificar el valor de una clave
diccionario['a'] = 10
print(diccionario)

# Añadir un nuevo elemento al diccionario
diccionario['f'] = 6
print(diccionario)

# Eliminar un elemento del diccionario
del diccionario['f']
print(diccionario)

# Comprobar si una clave existe en el diccionario
print('a' in diccionario)
print('f' in diccionario)

# Comprobar si una clave no existe en el diccionario
print('a' not in diccionario)
print('f' not in diccionario)

# Acceder a un elemento que no existe en el diccionario
try:
    print(diccionario['f'])
except KeyError as e:
    print(e)

# Acceder a un elemento que no existe en el diccionario con get
print(diccionario.get('f'))

# Acceder a un elemento que no existe en el diccionario con get y un valor por defecto
print(diccionario.get('f', 'No existe')) # No existe

# Acceder a un elemento que no existe en el diccionario con setdefault
print(diccionario.setdefault('f', 6)) 
# Devuelve el valor por defecto si la clave no existe y lo añade al diccionario
print(diccionario) # {'a': 10, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# El método update permite añadir varios elementos a la vez
diccionario.update({'g': 7, 'h': 8, 'i': 9})
print(diccionario)

# El método pop permite eliminar un elemento del diccionario
print(diccionario.pop('g'))

# El método popitem permite eliminar el último elemento del diccionario
print(diccionario.popitem())

# El método clear permite eliminar todos los elementos del diccionario
diccionario.clear()
print(diccionario)

# El método keys permite obtener las claves del diccionario
diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(diccionario.keys())

# El método values permite obtener los valores del diccionario
print(diccionario.values())

# El método items permite obtener los elementos del diccionario
print(diccionario.items())

# El método copy permite copiar un diccionario
diccionario_copia = diccionario.copy()
print(diccionario_copia)

# El método fromkeys permite crear un diccionario a partir de una lista de claves
claves = ['a', 'b', 'c', 'd', 'e']
diccionario = dict.fromkeys(claves)
print(diccionario)

# El método fromkeys permite crear un diccionario a partir de una lista de claves con un valor por defecto
diccionario = dict.fromkeys(claves, 0)
print(diccionario)

# Recorrer un diccionario con un bucle for
diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
for clave in diccionario:
    print(clave, diccionario[clave])

# Recorrer un diccionario con un bucle for y el método items
for clave, valor in diccionario.items():
    print(clave, valor)

# Recorrer un diccionario con un bucle for y el método keys
for clave in diccionario.keys():
    print(clave, diccionario[clave])

# Recorrer un diccionario con un bucle for y el método values
for valor in diccionario.values():
    print(valor)

# Recorrer un diccionario con un bucle while
diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
claves = list(diccionario.keys())
i = 0
while i < len(claves):
    clave = claves[i]
    print(clave, diccionario[clave])
    i += 1

