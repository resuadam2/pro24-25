# Alcance de las variables

# En Python, las variables pueden ser locales o globales. 
# Una variable local es aquella que se declara dentro de una función y solo puede ser utilizada dentro de ella. 
# Una variable global es aquella que se declara fuera de una función y puede ser utilizada en cualquier parte del programa.

# En el siguiente ejemplo, la variable x es local a la función suma y la variable 'y' es global:

def suma(a, b):
    x = a + b
    return x
# print(x) # Error: x no está definida
y = suma(3, 2)
print(suma(3, 2)) # Imprime 5
print(y) # Imprime 5

# La palabra reservada global se utiliza para declarar una variable global dentro de una función. 
# En el siguiente ejemplo, la variable 'y' es global:

def suma(a, b):
    global y
    y = a + b
    return y

y = 7
print(suma(3, 2)) # Imprime 5

print(y) # Imprime 5

# En Python, las variables locales tienen prioridad sobre las variables globales.
def suma(a, b):
    x = a + b
    return x

x = suma(3, 8)
print(suma(3, 2)) # Imprime 5
print(x) # Imprime 11
