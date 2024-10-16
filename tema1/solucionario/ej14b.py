# Ejercicio 14 -- versión pidiendo continuamente los números
"""
Diseñar un algoritmo que calcule la potencia para 
dos números naturales x e y mediante una acumulación
sucesiva de productos. Previo al cálculo se verificará 
que ambos valores son positivos.
"""
# Pedimos el número base hasta que sea positivo
base = -1
while base < 0:
    print("Introduzca el número base: ") # Pedimos el número base
    base = int(input()) # Leemos el número base
# Pedimos el número exponente hasta que sea positivo
exponente = -1
while exponente < 0:
    print("Introduzca el número exponente: ") # Pedimos el número exponente
    exponente = int(input()) # Leemos el número exponente
resultado = 1
for x in range(exponente): # Bucle para calcular la potencia
    resultado *= base # Calculamos la potencia
print("El resultado de elevar ", base, " a ", exponente, " es ", resultado)
