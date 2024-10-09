# calculo del factorial

n = int(input("Introduce un número para calcular su factorial: "))

factorial = n
i = n
while i > 1:
    i -= 1
    factorial *= i

print(f"El factorial de {n} es {factorial}")