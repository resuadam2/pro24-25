# versión sencilla del ejercicio
suma_pares = 0
suma_impares = 0
n_pares = 0

for i in range(10):
    num = int(input("Introduzca un número: "))
    if num % 2 == 0:
        suma_pares += num
        n_pares += 1
    else:
        suma_impares += num

print("La suma de los números pares es:", suma_pares)
print("La cantidad de pares es:", n_pares)
print("La media de los impares es:", suma_impares / (10 - n_pares))

# versión avanzada del ejercicio pidiendo el numero de veces que se van a introducir números

suma_pares = 0
suma_impares = 0
n_pares = 0

n_vueltas = int(input("Introduzca el número de veces que va a introducir números: "))

if n_vueltas <= 0:
    print("El número de veces debe ser mayor que 0")
else:
    for i in range(n_vueltas):
        num = int(input("Introduzca un número: "))
        if num % 2 == 0:
            suma_pares += num
            n_pares += 1
        else:
            suma_impares += num
    print("La suma de los números pares es:", suma_pares)
    print("La cantidad de pares es:", n_pares)
    print("La media de los impares es:", suma_impares / (n_vueltas - n_pares))