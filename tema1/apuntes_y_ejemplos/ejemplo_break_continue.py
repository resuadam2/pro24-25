# La sentencia break

""" La sentencia break se utiliza para salir de un bucle, independientemente de si se ha completado o no la iteración actual. 
En otras palabras, la sentencia break interrumpe la ejecución del bucle y pasa a la siguiente instrucción después del bucle. """
# Ejemplo en un bucle for
for i in range(1, 11):
    if i == 5:
        break
    print(i)

print("--------------------")

# Ejemplo en un bucle while
i = 1
while i < 11:
    if i == 5:
        break
    print(i)
    i += 1

""" Los break son especialmente útiles cuando se necesita salir de un bucle en función de una condición específica.   
En el ejemplo anterior, el bucle for se detiene cuando i es igual a 5. """

print("--------------------")

# La sentencia continue
""" La sentencia continue se utiliza para omitir el resto de las instrucciones en la iteración actual y pasar a la siguiente iteración del bucle.
"""
# Ejemplo en un bucle for
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

print("--------------------")

# Ejemplo en un bucle while
i = 1
while i < 11:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1

""" En el ejemplo anterior, el bucle for omite la impresión de 5 y continúa con el resto de las iteraciones.
El bucle while hace lo mismo, pero también incrementa la variable de control i en 1. """

print("--------------------")

# La sentencia pass
""" La sentencia pass se utiliza para evitar errores de sintaxis cuando no se requiere ningún código.
"""
# Ejemplo en un bucle for
for i in range(1, 11):
    pass

print("--------------------")

# Ejemplo en un bucle while
i = 1
while i < 11:
    pass
    i += 1

""" En el ejemplo anterior, el bucle for y el bucle while no hacen nada, pero no generan errores de sintaxis. """