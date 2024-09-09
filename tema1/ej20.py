# Ejercicio 20

"""
Diseñar un algoritmo que lea un número entero de teclado, 
visualice sus dígitos y calcule la suma de los dígitos que
sean pares. Para extraer los dígitos de un número usaremos
un bucle que divida el número por 10 sucesivamente.
El resto de cada división corresponde a cada uno de los dígitos.
"""
print("Introduzca un número entero: ") # Pedimos el número  
numero = int(input()) # Leemos el número
suma_pares = 0 # Inicializamos la variable suma_pares
while numero > 0: # Bucle para extraer los dígitos
    digito = numero % 10 # Extraemos el dígito
    print(digito) # Mostramos el dígito
    if digito % 2 == 0: # Si el dígito es par
        suma_pares += digito # Sumamos el dígito a la suma_pares
    numero = numero // 10 # Eliminamos el dígito
print("La suma de los dígitos pares es ", suma_pares) # Mostramos la suma_pares 
