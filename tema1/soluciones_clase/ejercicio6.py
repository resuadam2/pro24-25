# Ejercicio 6
"""
Diseñar un algoritmo que obtenga el promedio de una lista de varlores reales leídos por teclado. El algoritmo
terminará cuándo el usuario introduzca 20 valores.
"""
n = int(input("Ingrese el número de valores reales, para calcular su promedio: "))
suma = 0
contador = 0
while contador < n:
    valor = float(input("Ingrese un valor " + str(contador + 1) + "/" + str(n) + ": "))
    suma += valor
    contador += 1

promedio = suma / n
print("El promedio es: " + str(promedio))