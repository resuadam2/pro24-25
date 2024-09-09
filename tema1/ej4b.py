# Ejercicio 4 - versión avanzada tema 3
"""
Diseñar un algoritmo que lea 20 caracteres
de teclado y muestre por pantalla el número
de veces que se repiten cada una de las vocales
"""
vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0} # Diccionario con las vocales
print("Introduzca 20 caracteres: ") # Pedimos los caracteres
for x in range(20): # Bucle para leer los 20 caracteres
    caracter = input() # Leemos un caracter
    if caracter in vocales: # Si el caracter es una vocal
        vocales[caracter] += 1 # Incrementamos el contador de la vocal
for vocal in vocales: # Recorremos el diccionario
    print("La vocal", vocal, "se repite", vocales[vocal], "veces") # Mostramos el resultado

