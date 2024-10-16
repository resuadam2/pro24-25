# Ejercicio 7
"""
Diseñar un algoritmo que calcule y muestre en pantalla
el factorial de un número entero dado.
"""
print("Introduzca un número entero: ") # Pedimos el número  
numero = int(input()) # Leemos el número
factorial = 1 # Inicializamos el factorial a 1
for x in range(1, numero+1): # Bucle para calcular el factorial
    factorial *= x # Calculamos el factorial
print("El factorial de ", numero, " es ", factorial) # Mostramos el resultado
