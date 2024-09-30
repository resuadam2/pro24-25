# Funciones en python

# Definición
# Una función es un bloque de código que realiza una tarea específica.
# Para definir una función en Python, se utiliza la palabra reservada def seguida del nombre de la función y paréntesis ().

# Sintaxis
# def nombre_de_la_funcion(parametros):
#     # Código de la función
#     return valor_de_retorno
#
# nombre_de_la_funcion(parametros)

# Ejemplo

def saludar():
    print("Hola, mundo!")

saludar()

# Parámetros

# Los parámetros son valores que se pasan a la función para que realice una tarea específica.
# Los parámetros se definen entre los paréntesis de la función.
# Los parámetros pueden ser de cualquier tipo de datos.
# Los parámetros son opcionales.

# Ejemplo

def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Juan")

# Retorno de valores

# Una función puede devolver un valor utilizando la palabra reservada return.
# El valor de retorno puede ser de cualquier tipo de datos.
# Una función puede devolver múltiples valores utilizando una tupla.

# Ejemplo

def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(resultado)

# Ejemplo

def sumar_y_restar(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

resultado = sumar_y_restar(5, 3)
print(resultado)

# Funciones anónimas (lambda)

# Una función anónima es una función que no tiene nombre.
# Se define utilizando la palabra reservada lambda.
# Se utiliza para funciones pequeñas y sencillas.
# Se utiliza para funciones que se van a utilizar una sola vez.

# Sintaxis
# lambda parametros: expresion

# Ejemplo

suma = lambda a, b: a + b

resultado = suma(5, 3)
print(resultado)

# Ejemplo

cuadrado = lambda x: x ** 2

resultado = cuadrado(5)

print(resultado)

# Funciones predefinidas

# Python tiene muchas funciones predefinidas que se pueden utilizar sin necesidad de importar ningún módulo.

# Ejemplo

print(abs(-5)) # Valor absoluto
print(max(5, 3, 8)) # Valor máximo
print(min(5, 3, 8)) # Valor mínimo
print(pow(2, 3)) # Potencia
print(round(3.14159, 2)) # Redondeo

# Módulos

# Un módulo es un archivo que contiene funciones, clases y variables.
# Python tiene muchos módulos predefinidos que se pueden importar y utilizar en un programa.
# Para importar un módulo se utiliza la palabra reservada import seguida del nombre del módulo.

# Ejemplo

import math

print(math.pi)
print(math.sqrt(25))

# Ejemplo

from math import pi, sqrt

print(pi)
print(sqrt(25))

# Ejemplo

from math import * # Importa todas las funciones del módulo

print(pi)
print(sqrt(25))

# Ejemplo

import math as m # Importa el módulo con un alias

print(m.pi)
print(m.sqrt(25))

# Ejemplo

from math import pi as p, sqrt as s # Importa funciones con alias

print(p)
print(s(25))

# Ejemplo

import random

print(random.randint(1, 10)) # Número aleatorio entre 1 y 10
print(random.choice(["a", "b", "c"])) # Elemento aleatorio

# Ejemplo

import datetime

print(datetime.datetime.now()) # Fecha y hora actual

# Ejemplo

import os

print(os.getcwd()) # Directorio actual
print(os.listdir()) # Lista de archivos y directorios

# Ejemplo

import sys

print(sys.argv) # Argumentos de la línea de comandos

# Ejemplo

import platform

print(platform.system()) # Sistema operativo
print(platform.release()) # Versión del sistema operativo

# Ejemplo

import subprocess

subprocess.run(["ls", "-l"]) # Ejecutar un comando

# Ejemplo

import requests

response = requests.get("https://www.google.com")

print(response.status_code) # Código de estado
print(response.text) # Contenido de la página

# Ejemplo

import json

data = '{"name": "John", "age": 30, "city": "New York"}'

json_data = json.loads(data)

print(json_data["name"])
print(json_data["age"])
print(json_data["city"])

