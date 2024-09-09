# Ejercicio 2
"""
Diseñar un algoritmo que calcule y muestre en pantalla
el volumen y el área de una esfera para un radio dado
"""
import math # Importamos la librería math para usar la constante pi
print("Introduzca el radio de la esfera: ") # Pedimos el radio
radio = float(input()) # Leemos el radio
volumen = (4/3)*math.pi*(radio**3) # Calculamos el volumen  
area = 4*math.pi*(radio**2) # Calculamos el área    
print("El volumen de la esfera es ", volumen, " y el área es ", area) # Mostramos el resultado    