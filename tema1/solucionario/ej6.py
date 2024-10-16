# Ejercicio 6
"""
Diseñar un algoritmo que obtenga el promedio de una
lista de varlores reales leídos por teclado. El algoritmo
terminará cuándo el usuario introduzca 20 valores.
"""
suma = 0 # Inicializamos la variable suma
contador = 0 # Inicializamos el contador
while contador < 20: # Bucle para leer 20 valores
    print("Introduzca un valor real: ") # Pedimos un valor real
    valor = float(input()) # Leemos el valor
    suma += valor # Sumamos el valor a la suma
    contador += 1 # Incrementamos el contador
promedio = suma/20 # Calculamos el promedio
print("El promedio de los 20 valores es ", promedio) # Mostramos el resultado   