# Ejercicio 17
"""
Diseñar un algoritmo que lea números enteros positivos de teclado
y sólo acepte como válidos aquellos que sean mayores que el anterior
número leído. El algoritmo terminará cuando se introduzca el 0.
"""

# Pedimos el primer número
print("Introduzca un número entero positivo (0 para salir): ")
num = int(input()) # Leemos el primer número
actualValido = num # Guardamos el primer número
while num != 0: # Mientras el número sea distinto de 0
    print("Número actual: " + str(actualValido)) # Mostramos el número actual
    print("Introduzca un número entero positivo (0 para salir): ") # Pedimos un número
    num = int(input()) # Leemos el número
    if num > actualValido: # Si el número es mayor que el anterior
        actualValido = num # Actualizamos el número
    else: # Si no
        print("Número no válido") # Mostramos un mensaje de error
