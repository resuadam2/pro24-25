# Ejercicio 1
""" 
Diseñar un algoritmo que convierta una
temperatura leída en grados Farenheit a 
grados Celsius, usando la fórmula: C=(5/9)*(F-32).
"""
print("Introduzca los grados Farenheit a convertir: ") # Pedimos los grados Farenheit   
farenheit = float(input()) # Leemos los grados Farenheit
celsius = (5/9)*(farenheit-32) # Calculamos los grados Celsius
print(farenheit, " grados Farenheit son ", celsius, " grados Celsius.") # Mostramos el resultado    