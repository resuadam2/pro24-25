# Ejercicio 9
"""
Diseñar un algoritmo que calcule la suma de todos los números
comprendidos entre 1 y 500 que cumplan la condición de ser 
múltiplos de 5 y de 7. Para verificar si un número X es múltiplo
de otro número Y, basta con comprobar si el resto de la división    
entera de X entre Y es igual a 0. 
"""
suma = 0 # Inicializamos la suma a 0
for x in range(1, 501): # Bucle para calcular la suma
    if x % 5 == 0 and x % 7 == 0: # Comprobamos si es múltiplo de 5 y 7
        suma += x # Sumamos el número a la suma
print("La suma de los números múltiplos de 5 y 7 entre 1 y 500 es ", suma) # Mostramos el resultado
