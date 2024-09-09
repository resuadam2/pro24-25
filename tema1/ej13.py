# Ejercicio 13
"""
Diseñar un algoritmo, que dados dos números, determine si su producto es positivo, 
nulo o negativo, sin realizar la multiplicación.    
"""
print("Introduzca el primer número: ") # Pedimos el primer número
num1 = int(input()) # Leemos el primer número
print("Introduzca el segundo número: ") # Pedimos el segundo número
num2 = int(input()) # Leemos el segundo número
if num1 > 0 and num2 > 0 or num1 < 0 and num2 < 0:
    print("El producto es positivo")
elif num1 == 0 or num2 == 0:
    print("El producto es nulo")
else:
    print("El producto es negativo")