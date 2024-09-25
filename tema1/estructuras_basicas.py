# Estructuras básicas de programación en Python

# Estructura secuencial
# Las instrucciones se ejecutan de arriba hacía abajo, una tras otra.

# Ejemplo 1 - Estructura secuencial
x = 5
y = 3
z = x + y
print(z)

print("--------------------")

# Ejemplo 2 - Estructura secuencial
nombre = "Juan"
apellido = "Pérez"
nombre_completo = nombre + " " + apellido
print(nombre_completo)

# Estructuras condicionales (if, elif, else)

# if condicion:
#     instrucciones
# elif condicion:
#     instrucciones
# else:
#     instrucciones

# Ejemplo 1 - Estructura condicional if
x = 10
if x > 5:
    print("x es mayor que 5")

print("--------------------")

# Ejemplo 2 - Estructura condicional if-else
x = 3
if x > 5:
    print("x es mayor que 5")
else:
    print("x es menor o igual a 5")

print("--------------------")

# Ejemplo 3 - Estructura condicional if-elif-else

x = 5
if x > 5:
    print("x es mayor que 5")
elif x == 5:
    print("x es igual a 5")
else:
    print("x es menor que 5")

print("--------------------")

# Estructura condicional if anidada
# if condicion:
#     instrucciones
#     if condicion:
#         instrucciones

# Ejemplo 1 - Estructura condicional if anidada
x = 10
if x > 5:
    print("x es mayor que 5")
    if x == 10:
        print("x es igual a 10")

print("--------------------")

# Estructura match-case
# match expresion:
#     case valor1:
#         instrucciones
#     case valor2:
#         instrucciones
#     case _:
#         instrucciones

# Ejemplo 1 - Estructura match-case
x = 5
match x:
    case 1:
        print("x es igual a 1")
    case 2:
        print("x es igual a 2")
    case 3:
        print("x es igual a 3")
    case _:
        print("x no es igual a 1, 2 o 3")

print("--------------------")


# Estructuras repetitivas (bucles)

# Bucle while
# while condicion:
#     instrucciones

# Ejemplo 1 - Bucle while
i = 1
while i < 6:
    print(i)
    i += 1

print("--------------------")
# Ejemplo 2 - Bucle while
i = 10
while i > 0:
    print(i)
    i -= 1

print("--------------------")

# Ejemplo 3 - Bucle while recorriendo una string
palabra = "Python"
i = 0
while i < len(palabra):
    print(palabra[i])
    i += 1



# Bucle for
# for variable in secuencia:
#     instrucciones

# Ejemplo 1 - Bucle for 
for i in range(3):
    print(i)

print("--------------------")
# Ejemplo 2 - Bucle for
for i in range(1,6):
    print(i)

print("--------------------")
# Ejemplo 3 - Bucle for
for i in range(1,11,3):
    print(i)

print("--------------------")
# Ejemplo 4 - Bucle for
for i in range(10,0,1):
    print(i)

print("--------------------")
# Ejemplo 5
palabra = "Python"
print(len(palabra))
for letra in palabra:
    print(letra, end="-")
print("\n--------------------")

# Bucle for anidado
# for variable1 in secuencia1:
#     instrucciones
#     for variable2 in secuencia2:
#         instrucciones

# Ejemplo 1 - Bucle for anidado
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
