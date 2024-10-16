# Realizar un algoritmo que pinte la letra U por pantalla hecha con asteriscos.
# El programa pedirá la altura. 
# Fíjate que el programa inserta un espacio y pinta dos asteriscos menos en la base
# para simular la curvatura de la letra.
# Es importante indicar al usuario que la altura mínima debe ser de 4.
# 
# Ejemplo 1:
# Introduzca la altura de la U: 5
# 
# *     *
# *     *
# *     *
# *     *
#   *** 
# Ejemplo 2:

# Introduzca la altura de la U: 4

# *    *
# *    *
# *    *
#   **

# Solución:

altura = int(input("Introduzca la altura de la U: "))

if altura < 4:
    print("La altura mínima debe ser de 4")
else:
    for i in range(altura):
        if i == altura - 1: # Si estamos en la base
            print("   " + "*" * (altura- 2))
        else: # Si estamos en el resto de la letra
            print(" *" + " " * (altura) + "*")
print("Fin del programa") # Mostramos el mensaje de fin de programa

# Solución usando else sin el if:

altura = int(input("Introduzca la altura de la U: "))

if altura < 4:
    print("La altura mínima debe ser de 4")
else:
    for i in range(altura - 1):
        # Si estamos en el resto de la letra
        print(" *" + " " * (altura) + "*")
    else: # Si estamos en la base
        print("   " + "*" * (altura - 2))
print("Fin del programa") # Mostramos el mensaje de fin de programa
