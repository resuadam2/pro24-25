valores_positivos = False
print("Calculo de la potencia")
while not valores_positivos:
    a = input("Ingrese un número entero positivo como base: ")
    b = input("Ingrese otro número entero positivo como exponente: ")
    if a.isdigit() and b.isdigit(): 
        a = int(a)
        b = int(b)
        if a > 0 and b > 0:
            valores_positivos = True
        else:
            print("Ingrese valores positivos")
    else:
        print("Ingrese solo números enteros positivos")

potencia = a
for i in range(1,b):
    potencia = potencia * a

print("El resultado de la potencia es: ", potencia)

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