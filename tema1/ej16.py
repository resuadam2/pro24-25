# Ejercicio 16
"""
Diseñar un algoritmo que pida al usuario un número del 1 al 9 y le
conteste diciendo si el número es primo o no. Por ejemplo, si el 
usuario introduce el número 7, el algoritmo le responderá que 7 es  
un número primo.
"""

print("Introduzca un número del 1 al 9: ") # Pedimos el número
numero = int(input()) # Leemos el número
if numero == 4 or numero == 6 or numero == 8 or numero == 9:
    print("El número no es primo")
else:
    print("El número es primo")
