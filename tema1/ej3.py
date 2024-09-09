# Ejercicio 3 -- version con ifs
"""
Diseñar un algoritmo que pida una nota (valor entero)
por teclado y dependiendo de su valor visualice la nota
en letras. Por ejemplo, si nota es igual a 7 tiene que 
mostrar el texto "Notable".
"""
print("Introduzca la nota (0-10 valores enteros): ") # Pedimos la nota  
nota = int(input()) # Leemos la nota
if nota >= 0 and nota < 5: # Comprobamos si la nota es insuficiente
    print("Insuficiente") # Mostramos un mensaje
if nota >= 5 and nota < 6:
    print("Suficiente")
if nota >= 6 and nota < 7:
    print("Bien")
if nota >= 7 and nota < 9:
    print("Notable")
if nota >= 9 and nota <= 10:
    print("Sobresaliente")
if nota < 0 or nota > 10:
    print("Nota no válida")

