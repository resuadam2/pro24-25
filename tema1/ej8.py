# Ejercicio 8
"""
Realizar un algoritmo que calcule y muestre en la pantalla la suma 
de los n primeros enteros impares. El valor de n se solicitará al usuario.
"""
print("Introduzca un número entero: ") # Pedimos el número  
n = int(input()) # Leemos el número
suma = 0 # Inicializamos la suma a 0
contador = 0 # Inicializamos el contador a 0
numero = 1 # Inicializamos el primer número impar
while contador < n: # Bucle para calcular la suma
    suma += numero # Sumamos el número a la suma
    numero += 2 # Calculamos el siguiente número impar
    contador += 1 # Incrementamos el contador
print("La suma de los ", n, " primeros enteros impares es ", suma) # Mostramos el resultado
