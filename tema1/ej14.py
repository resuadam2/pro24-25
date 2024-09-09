# Ejercicio 14
"""
Diseñar un algoritmo que calcule la potencia para 
dos números naturales x e y mediante una acumulación
sucesiva de productos. Previo al cálculo se verificará 
que ambos valores son positivos.
"""
print("Introduzca el número base: ") # Pedimos el número base
base = int(input()) # Leemos el número base
print("Introduzca el número exponente: ") # Pedimos el número exponente
exponente = int(input()) # Leemos el número exponente
if base < 0 or exponente < 0: # Si alguno de los números es negativo
    print("Los números deben ser positivos") # Mostramos un mensaje de error
else:
    resultado = 1
    for x in range(exponente):
        resultado *= base
    print("El resultado de elevar ", base, " a ", exponente, " es ", resultado)
    