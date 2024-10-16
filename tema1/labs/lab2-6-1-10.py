# Laboratorio 2.6.1.10: Operadores y expresiones

"""
La tarea es completar el código para evaluar la expresión siguiente:
1/(x + 1/(x + 1/(x + 1/x)))
El resultado debe ser asignado a la variable y.
"""

x = float(input("Ingresa el valor para x: "))

# Escribe tu código aquí.
y = 1 / (x + 1 / (x + 1 / (x + 1 / x)))
print("y =", y)
