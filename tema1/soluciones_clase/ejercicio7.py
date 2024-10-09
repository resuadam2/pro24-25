# El factorial de 4 es 24: 4*3*2*1 = 24

n = int(input("Introduce un número para calcular su factorial: "))

factorial = 1

for i in range(1, n+1):
    factorial *= i # es lo mismo que factorial = factorial * i

print(f"El factorial de {n} es {factorial}")
# print("El factorial de", n, "es", factorial) # Otra forma de hacerlo