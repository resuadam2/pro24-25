# Ejercicio 3 -- version con match-case
"""
Diseñar un algoritmo que pida una nota (valor entero)
por teclado y dependiendo de su valor visualice la nota
en letras. Por ejemplo, si nota es igual a 7 tiene que 
mostrar el texto "Notable".
"""
print("Introduzca la nota (0-10 valores enteros): ") 
nota = int(input()) # Leemos la nota
match nota: # Comprobamos la nota
    case 0 | 1 | 2 | 3 | 4: # Si la nota es menor que 5
        print("Insuficiente") # Mostramos un mensaje
    case 5: 
        print("Suficiente")
    case 6:
        print("Bien")
    case 7 | 8:
        print("Notable")
    case 9 | 10:
        print("Sobresaliente")
    case _:
        print("Nota no válida")

