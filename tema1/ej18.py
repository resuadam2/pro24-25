# Ejercicio 18
"""
Diseñar un algoritmo que lea una lista de 10 números enteros, 
visualice la suma de los pares, cuántos pares existen y cuál
es la media aritmética de los números impares.  
"""

suma_pares = 0 # Inicializamos la variable suma_pares
contador_pares = 0 # Inicializamos el contador_pares
suma_impares = 0 # Inicializamos la variable suma_impares
print("Introduzca 10 números enteros: ") # Pedimos 10 números enteros
for x in range(10): # Bucle para leer 10 valores
    # Pedimos un número entero y mostramos usando x+1 para que el usuario sepa cuántos números lleva    
    print("Introduzca un número entero: " + str((x+1)) + "/10") # Pedimos un número entero
    num = int(input()) # Leemos el número
    if num % 2 == 0: # Si el número es par
        suma_pares += num # Sumamos el número a la suma_pares
        contador_pares += 1 # Incrementamos el contador_pares
    else: # Si el número es impar
        suma_impares += num # Sumamos el número a la suma_impares   
if contador_pares == 10: # Si no hay pares
    media_impares = 0 # La media_impares es 0
else: # Si hay pares
    media_impares = suma_impares/(10-contador_pares) # Calculamos la media_impares  
print("La suma de los pares es ", suma_pares) # Mostramos la suma_pares 
print("Existen ", contador_pares, " pares") # Mostramos el contador_pares   
print("La media de los impares es ", media_impares) # Mostramos la media_impares    

"""
str() convierte un número a cadena de texto 
"""