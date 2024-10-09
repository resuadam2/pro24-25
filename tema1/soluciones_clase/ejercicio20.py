sum_pares = 0

num = int(input("Introduzca un número: "))

while num != 0:
    digito = num % 10
    if digito % 2 == 0:
        sum_pares += digito
    num //= 10 # num = num // 10 - le estoy quitando el dígito que acabamos de comprobar (el de más a la derecha)
    if num != 0:
        print("Digito:", digito, ", ", end="")
    else:
        print("Digito:", digito, ".")

print("La suma de los dígitos pares es:", sum_pares)

# Version mostrando de izquierda a derecha los numeritos (no es necesario)

num = int(input("Introduzca un número: "))
muestra = ""

while num != 0:
    digito = num % 10
    if digito % 2 == 0:
        sum_pares += digito
    num //= 10 # num = num // 10 - le estoy quitando el dígito que acabamos de comprobar (el de más a la derecha)
    muestra = str(digito) + " " + muestra

print("Dígitos:", muestra)