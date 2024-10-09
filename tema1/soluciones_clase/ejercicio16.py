# Ejercicio 16 - Primos entre el 1 y el 9
# Versión sencilla y de andar por casa
num = int(input("Introduzca un número (1-9): ")) # Pedimos un número

if num < 1 or num > 9:
    print("Número no válido")
elif num == 1 or num == 4 or num == 6 or num >= 8:
    print("No es primo")
else:
    print("Es primo")

# Versión que nos sirva para cualquier número

num = int(input("Introduzca un número positivo: ")) # Pedimos un número

for i in range(2, num): # Bucle para comprobar si es primo
    if num % i == 0: # Si el número es divisible por i
        print("No es primo") # Mostramos que no es primo
        break # Salimos del bucle
else:
    print("Es primo")
print("Fin del programa") # Mostramos el mensaje de fin de programa

# Versión con while

num = int(input("Introduzca un número positivo: ")) # Pedimos un número
i = 2 # Inicializamos el divisor
if num == 1:
    print("No es primo")
else:
    while i < num: # Mientras el divisor sea menor que el número
        if num % i == 0: # Si el número es divisible por i
            print("No es primo") # Mostramos que no es primo
            break # Salimos del bucle
        i += 1 # Incrementamos el divisor
    else:
        print("Es primo")