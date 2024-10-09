# Ejercicio 15

"""
Diseñar un algoritmo que lea una secuencia de 20 números reales introducidos por teclado.
Al acabar la secuencia, debe mostrar el número mayor y el número menor de los introducidos.
"""
max = float(input("Introduzca un número: ")) # Pedimos el primer número
min = max # Inicializamos el mínimo al primer número

for i in range(19): # Bucle para leer los 19 números restantes
    num = float(input("Introduzca un número: ")) # Pedimos un número
    if num > max: # Si el número es mayor que el máximo
        max = num # Actualizamos el máximo
    if num < min: # Si el número es menor que el mínimo
        min = num # Actualizamos el mínimo

print("El número mayor es ", max) # Mostramos el número mayor
print("El número menor es ", min) # Mostramos el número menor
