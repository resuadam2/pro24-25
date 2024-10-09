# Ejercicio 17 
num = -1
while num < 0:
    num = int(input("Introduzca un número positivo: ")) # Pedimos un número
    if num < 0:
        print("El número introducido no es positivo")

while num != 0:
    print("Pulse 0 para salir.")
    aux = int(input("Introduzca un número mayor que el actual (" + str(num) + "):\n")) # Pedimos un número
    if aux > num:
        num = aux
    elif aux == 0:
        break
    else:
        print("El número introducido no es mayor que el actual")
print("Fin del programa") # Mostramos el mensaje de fin de programa