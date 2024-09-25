# Operadores básicos en Python

# Operadores aritméticos
# Los operadores aritméticos se utilizan para realizar operaciones matemáticas.

# Suma (+)
# Resta (-)
# Multiplicación (*)
# División (/)
# Módulo (%)
# Potencia (**)
# División entera (//)

# Ejemplo de operadores aritméticos
# Suma
a = 5
b = 3
c = a + b
print(c)

# Resta
a = 5
b = 3
c = a - b
print(c)

# Multiplicación
a = 5
b = 3
c = a * b
print(c)

# División
a = 5
b = 3
c = a / b
print(c)

# Módulo
a = 5
b = 3
c = a % b
print(c)

# Potencia
a = 5
b = 3
c = a ** b
print(c)

# División entera
a = 5
b = 3
c = a // b
print(c)

# Operadores de comparación
# Los operadores de comparación se utilizan para comparar dos valores.

# Igual a (==)
# Diferente de (!=)
# Mayor que (>)
# Menor que (<)
# Mayor o igual que (>=)
# Menor o igual que (<=)

# Ejemplo de operadores de comparación

# Igual a
a = 5
b = 3
if a == b:
    print("a es igual a b")
else:
    print("a no es igual a b")

# Diferente de
a = 5
b = 3
if a != b:
    print("a es diferente de b")
else:
    print("a es igual a b")

# Mayor que
a = 5
b = 3
if a > b:
    print("a es mayor que b")
else:
    print("a no es mayor que b")

# Menor que
a = 5
b = 3
if a < b:
    print("a es menor que b")
else:
    print("a no es menor que b")

# Mayor o igual que
a = 5
b = 3
if a >= b:
    print("a es mayor o igual que b")
else:
    print("a es menor que b")

# Menor o igual que
a = 5
b = 3
if a <= b:
    print("a es menor o igual que b")
else:
    print("a es mayor que b")

# Operadores lógicos
# Los operadores lógicos se utilizan para combinar expresiones lógicas.

# and
# or
# not

# Ejemplo de operadores lógicos

# and
a = 5
b = 3
c = 7
if a > b and a < c:
    print("a es mayor que b y menor que c")
else:
    print("a no cumple con las condiciones")

# or
a = 5
b = 3
c = 7
if a > b or a > c:
    print("a es mayor que b o mayor que c")
else:
    print("a no cumple con las condiciones")

# not
a = 5
b = 3
if not a == b: # seria lo mismo que a != b
    print("a no es igual a b")
else:
    print("a es igual a b")

# Operadores de asignación
# Los operadores de asignación se utilizan para asignar un valor a una variable.

# = (asignación)
# += (suma y asignación)
# -= (resta y asignación)
# *= (multiplicación y asignación)
# /= (división y asignación)
# %= (módulo y asignación)
# **= (potencia y asignación)
# //= (división entera y asignación)

# Ejemplo de operadores de asignación

# =
a = 5
print(a)

# +=
a = 5
a += 3 # a = a + 3
print(a)

# -=
a = 5
a -= 3
print(a)

# *=
a = 5
a *= 3
print(a)

# /=
a = 5
a /= 3
print(a)

# %=
a = 5
a %= 3
print(a)

# **=
a = 5
a **= 3
print(a)

# //=
a = 5
a //= 3
print(a)

# Operadores de identidad
# Los operadores de identidad se utilizan para comparar la identidad de dos objetos.

# is
# is not

# Ejemplo de operadores de identidad

a = 5
b = 5
if a is b:
    print("a y b son el mismo objeto")
else:
    print("a y b no son el mismo objeto")

a = 5
b = 3
if a is not b:
    print("a y b no son el mismo objeto")
else:
    print("a y b son el mismo objeto")

# Operadores de pertenencia
# Los operadores de pertenencia se utilizan para comprobar si un objeto está presente en una secuencia.

# in
# not in

# Ejemplo de operadores de pertenencia

lista = [1, 2, 3, 4, 5]
a = 3
if a in lista:
    print("a está en la lista")
else:
    print("a no está en la lista")

lista = [1, 2, 3, 4, 5]
a = 6
if a not in lista:
    print("a no está en la lista")
else:
    print("a está en la lista")

# Operadores de bits
# Los operadores de bits se utilizan para realizar operaciones a nivel de bits.

# & (AND)
# | (OR)
# ^ (XOR)
# ~ (NOT)
# << (desplazamiento a la izquierda)
# >> (desplazamiento a la derecha)

# Ejemplo de operadores de bits

# &
a = 5
b = 3
c = a & b
print(c)

# |
a = 5
b = 3
c = a | b
print(c)

# ^
a = 5
b = 3
c = a ^ b
print(c)

# ~
a = 5
c = ~a
print(c)

# <<
a = 5
c = a << 1
print(c)

# >>
a = 5
c = a >> 1
print(c)