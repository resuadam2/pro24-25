# Ejercicio 4
"""
Diseñar un algoritmo que lea 20 caracteres
de teclado y muestre por pantalla el número
de veces que se repiten cada una de las vocales.
"""
# Pedimos los caracteres
a = 0 # Contador de la vocal a
e = 0 # Contador de la vocal e
i = 0 # Contador de la vocal i
o = 0 # Contador de la vocal o
u = 0 # Contador de la vocal u
print("Introduzca 20 caracteres: ") # Pedimos los caracteres    
for x in range(20): # Bucle para leer los 20 caracteres
    caracter = input() # Leemos un caracter
    if caracter == "a": # Si el caracter es una vocal
        a += 1 # Incrementamos el contador de la vocal
    elif caracter == "e": 
        e += 1
    elif caracter == "i":
        i += 1
    elif caracter == "o":
        o += 1
    elif caracter == "u":
        u += 1
print("La vocal a se repite ", a, " veces") # Mostramos el resultado
print("La vocal e se repite ", e, " veces")
print("La vocal i se repite ", i, " veces")
print("La vocal o se repite ", o, " veces")
print("La vocal u se repite ", u, " veces")
