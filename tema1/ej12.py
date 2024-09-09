# Ejercicio 12
"""
Diseñar un algoritmo que lea del teclado tres números
enteros y escriba en pantalla un mensaje indicando si
al menos dos de esos tres números son pares.
"""
print("Introduzca el primer número: ") # Pedimos el primer número
num1 = int(input()) # Leemos el primer número
print("Introduzca el segundo número: ") # Pedimos el segundo número
num2 = int(input()) # Leemos el segundo número
print("Introduzca el tercer número: ") # Pedimos el tercer número
num3 = int(input()) # Leemos el tercer número
if num1 % 2 == 0 and num2 % 2 == 0 or num1 % 2 == 0 and num3 % 2 == 0 or num2 % 2 == 0 and num3 % 2 == 0:
    print("Al menos dos de los tres números son pares")
else:
    print("No hay al menos dos números pares")
