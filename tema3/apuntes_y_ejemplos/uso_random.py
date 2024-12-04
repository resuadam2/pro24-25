# Uso de random en Python

# En Python, el módulo random nos permite generar números aleatorios. 
# Para ello, primero debemos importar el módulo con la instrucción import random. 
# A continuación, podemos utilizar las funciones que nos proporciona el módulo random para generar números aleatorios.

# Ejemplo de uso de random en Python:

import random

# Generar un número entero aleatorio entre 0 y 9

numero = random.randint(0, 9)
print(numero)

# Generar un número real aleatorio entre 0 y 1

numero_real = random.random()
print(numero_real)

# Generar un número real aleatorio entre 0 y 10

numero_real_10 = random.uniform(0, 10)
print(numero_real_10)

# Generar un número entero aleatorio entre 0 y 9

numero_entero = random.randrange(10)
print(numero_entero)

# Generar un número entero aleatorio entre 1 y 10

numero_entero_10 = random.randrange(1, 11)
print(numero_entero_10)

# Generar elementos aleatorios de una lista

lista = [1, 2, 3, 4, 5]
elemento = random.choice(lista)
print(elemento)

colores = ['rojo', 'verde', 'azul']
color = random.choice(colores)
print(color)

# Barajar los elementos de una lista

random.shuffle(lista)
print(lista)

# Generar una muestra aleatoria de una lista
muestra = random.sample(lista, 3)
print(muestra)

