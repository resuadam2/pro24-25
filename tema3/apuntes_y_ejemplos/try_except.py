# Control de excepciones en Python

# Las excepciones son errores que ocurren durante la ejecución de un programa. 
# Cuando se produce una excepción, el programa se detiene y muestra un mensaje de error. 
# Para evitar que el programa se detenga, se pueden controlar las excepciones con bloques try-except.

# Bloque try-except

# El bloque try-except se utiliza para controlar las excepciones que se producen durante la 
# ejecución de un programa.

# Sintaxis:

# try:
#     # Código que puede producir una excepción
# except Excepción as e:
#     # Código que se ejecuta si se produce la excepción
# Ejemplo:

try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(e) # division by zero

# En este ejemplo, se produce una excepción ZeroDivisionError al intentar dividir un número por cero.

# El bloque try-except captura la excepción y muestra un mensaje de error.

# Bloque try-except-else

# El bloque try-except-else se utiliza para controlar las excepciones que se producen durante la
# ejecución de un programa y ejecutar un código adicional si no se produce ninguna excepción.

# Sintaxis:

# try:
#     # Código que puede producir una excepción
# except Excepción as e:
#     # Código que se ejecuta si se produce la excepción
# else:
#     # Código que se ejecuta si no se produce ninguna excepción
# Ejemplo:

try:
    x = 1 / 1
except ZeroDivisionError as e:
    print(e)
else:
    print('No se ha producido ninguna excepción')

# En este ejemplo, no se produce ninguna excepción al intentar dividir un número por uno.

# Captura de varias excepciones

# Se pueden capturar varias excepciones en un mismo bloque try-except.

# Sintaxis:

# try:
#     # Código que puede producir una excepción
# except Excepción1 as e:
#     # Código que se ejecuta si se produce la excepción1
# except Excepción2 as e:
#     # Código que se ejecuta si se produce la excepción2
# except Excepción3 as e:
#     # Código que se ejecuta si se produce la excepción3
# ...
# Ejemplo:

try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)

# En este ejemplo, se capturan dos excepciones: ZeroDivisionError y Exception.

# La excepción ZeroDivisionError se produce al intentar dividir un número por cero.

# La excepción Exception es la clase base de todas las excepciones en Python.

# Cuándo se capturan varias excepciones, se deben capturar primero las excepciones más específicas y 
# luego las excepciones más generales. 
# Si se captura primero una excepción más general, las excepciones más específicas no se capturan.
# Por ejemplo, si se captura primero la excepción Exception, no se captura la excepción ZeroDivisionError.
# Solo se captura una excepción en un bloque try-except y se ejecuta el código correspondiente.  

# Bloque try-except-finally

# El bloque try-except-finally se utiliza para controlar las excepciones que se producen durante la
# ejecución de un programa y ejecutar un código adicional al final del bloque try-except.

# Sintaxis:

# try:
#     # Código que puede producir una excepción
# except Excepción as e:
#     # Código que se ejecuta si se produce la excepción
# finally:
#     # Código que se ejecuta al final del bloque try-except
# Ejemplo:

try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(e)
finally:
    print('Bloque finally')

# En este ejemplo, se produce una excepción ZeroDivisionError al intentar dividir un número por cero.

# El bloque finally se ejecuta al final del bloque try-except. En este caso, se muestra un mensaje de error.

# Bloque try-except-else-finally

# El bloque try-except-else-finally se utiliza para controlar las excepciones que se producen durante la
# ejecución de un programa y ejecutar un código adicional si no se produce ninguna excepción y al final 
# del bloque try-except.

# Sintaxis:

# try:
#     # Código que puede producir una excepción
# except Excepción as e:
#     # Código que se ejecuta si se produce la excepción
# else:
#     # Código que se ejecuta si no se produce ninguna excepción
# finally:
#     # Código que se ejecuta al final del bloque try-except
# Ejemplo:

try:
    x = 1 / 1
except ZeroDivisionError as e:
    print(e)
else:
    print('No se ha producido ninguna excepción')
finally:
    print('Bloque finally')

# En este ejemplo, no se produce ninguna excepción al intentar dividir un número por uno.

# El bloque else se ejecuta si no se produce ninguna excepción.

# El bloque finally se ejecuta al final del bloque try-except. En este caso, se muestra un mensaje de error.

# Excepciones más comunes en Python

# ZeroDivisionError: Se produce al intentar dividir un número por cero.
# NameError: Se produce al intentar acceder a una variable que no está definida.
# TypeError: Se produce al intentar realizar una operación con un tipo de dato incorrecto.
# ValueError: Se produce al intentar realizar una operación con un valor incorrecto.
# KeyError: Se produce al intentar acceder a una clave que no existe en un diccionario.
# IndexError: Se produce al intentar acceder a un índice que no existe en una lista o tupla.
# FileNotFoundError: Se produce al intentar abrir un archivo que no existe.
# OSError: Se produce al intentar realizar una operación con un archivo que no existe.
# AttributeError: Se produce al intentar acceder a un atributo que no existe en un objeto.
# ImportError: Se produce al intentar importar un módulo que no existe.
# ModuleNotFoundError: Se produce al intentar importar un módulo que no existe.
# IndentationError: Se produce al intentar ejecutar un bloque de código con una indentación incorrecta.
# SyntaxError: Se produce al intentar ejecutar un código con una sintaxis incorrecta.

# Documentación oficial de Python sobre excepciones: https://docs.python.org/3/library/exceptions.html