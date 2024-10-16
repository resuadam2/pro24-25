# Ejercicio 3 -- version con elif
"""
Diseñar un algoritmo que pida una nota (valor entero)
por teclado y dependiendo de su valor visualice la nota
en letras. Por ejemplo, si nota es igual a 7 tiene que 
mostrar el texto "Notable".
"""
print("Introduzca la nota (0-10 valores enteros): ") # Pedimos la nota  
nota = int(input()) # Leemos la nota
if nota < 0 or nota > 10: # Comprobamos si la nota es válida
    print("Nota no válida") # Mostramos un mensaje de error
else: # Si la nota es válida
    if nota < 5: # Comprobamos si la nota es insuficiente
        print("Insuficiente") # Mostramos un mensaje
    elif nota == 5: # Comprobamos si la nota es suficiente
        print("Suficiente") # Mostramos un mensaje
    elif nota == 6:
        print("Bien")
    elif nota < 9:
        print("Notable")
    else:
        print("Sobresaliente")

