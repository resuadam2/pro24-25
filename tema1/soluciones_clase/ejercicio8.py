# suma de los N primeros impares

n = int(input("Introduzca la cantidad de impares que quiere sumar: "))

# Opcion 1

suma = 0

for i in range(1, n*2, 2):
    suma += i

print(f"La suma de los {n} primeros impares es {suma}")

# Opcion 2

suma = 0

for i in range(1, n+1):
    suma += 2*i-1

print(f"La suma de los {n} primeros impares es {suma}")

# Opcion 3

suma = 0
i = 1

while i <= n:
    suma += 2*i-1
    i += 1

print(f"La suma de los {n} primeros impares es {suma}")

# Opcion 4

suma = 0
i = 1

while i <= n*2:
    suma += i
    i += 2

print(f"La suma de los {n} primeros impares es {suma}")

# Opcion 5 con ifs

suma = 0
i = 1

while i <= n*2:
    if i % 2 != 0: # Si el número es impar
        suma += i
    i += 1

print(f"La suma de los {n} primeros impares es {suma}")