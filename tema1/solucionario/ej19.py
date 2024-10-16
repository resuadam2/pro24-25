# Ejercicio 19

"""
Diseñar un algoritmo que lea un conjunto de números reales, los cuente
y calcule y muestre la media, varianza y la desviación típica del conjunto
de números. La media y la varianza se calculan con las fórmulas:    
media = (suma de los números) / (número de números) 
varianza = ((suma de los cuadrados de los números) - (suma de los números)^2 / (número de números)) 
La desviación típica es la raíz cuadrada de la varianza.    
"""
import math # Importamos la librería math   
suma = 0 # Inicializamos la variable suma   
suma_cuadrados = 0 # Inicializamos la variable suma_cuadrados   
contador = 0 # Inicializamos el contador    
print("Introduzca un número real (0 para terminar): ") # Pedimos un número real 
num = float(input()) # Leemos un número real    
while num != 0: # Bucle para leer números reales
    suma += num # Sumamos el número a la suma
    suma_cuadrados += num**2 # Sumamos el cuadrado del número a la suma_cuadrados
    contador += 1 # Incrementamos el contador
    print("Introduzca un número real (0 para terminar): ") # Pedimos un número real
    num = float(input()) # Leemos un número real
if contador == 0: # Si no se han introducido números    
    print("No se han introducido números") # Mostramos un mensaje
else:
    media = suma/contador
    varianza = (suma_cuadrados - (suma**2)/contador)/contador   
    desviacion_tipica = math.sqrt(varianza) # Calculamos la desviación típica   
    print("La media es ", media)
    print("La varianza es ", varianza)
    print("La desviación típica es ", desviacion_tipica)

"""
math.sqrt() calcula la raíz cuadrada de un número   
"""