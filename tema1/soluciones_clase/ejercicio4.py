# Ejercicio 4
"""
Diseñar un algoritmo que lea 20 caracteres
de teclado y muestre por pantalla el número
de veces que se repiten cada una de las vocales.
"""
# Creamos contadores
a = 0
e = 0
i = 0
o = 0
u = 0

print("Ingrese 20 caracteres (si ingresa más de 20 no se tendrán en cuenta)")
caracteres = input().lower()
# asdfjbpoeiquvnqeoirvnodsaodsapeqrhgqeihrgcpqheirg
if len(caracteres) > 20:
    vueltas = 20
else:
    vueltas = len(caracteres)

for x in range(vueltas):
    match caracteres[x]:
        case "a":
            a += 1
        case "e":
            e += 1
        case "i":
            i += 1
        case "o":
            o += 1
        case "u":
            u += 1

print("Cantidad de vocales a: " + str(a))
print("Cantidad de vocales e: " + str(e))
print("Cantidad de vocales i: " + str(i))
print("Cantidad de vocales o: " + str(o))
print("Cantidad de vocales u: " + str(u))




"""
for x in range(20):
    caracter = ""
    while len(caracter) != 1:
        print("Ingrese un caracter: " + str(x+1) + "/20")
        caracter = input().lower()
        if len(caracter) != 1:
            print("Debe ingresar solo un único caracter")
    match caracter:
        case "a":
            a += 1
        case "e":
            e += 1
        case "i":
            i += 1
        case "o":
            o += 1
        case "u":
            u += 1

    print("Cantidad de vocales a: " + str(a))
    print("Cantidad de vocales e: " + str(e))
    print("Cantidad de vocales i: " + str(i))
    print("Cantidad de vocales o: " + str(o))
    print("Cantidad de vocales u: " + str(u))
"""