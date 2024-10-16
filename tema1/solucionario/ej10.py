# Ejercicio 10
"""
Implementar un programa que verifique si un texto es "Twiteable"
(tiene 280 caracteres o menos) o no. El programa debe pedir un texto    
por teclado y mostrar un mensaje indicando si el texto es Twiteable o no.   
"""
print("Introduzca un texto: ") # Pedimos un texto
texto = input() # Leemos el texto
if len(texto) <= 280: # Comprobamos si el texto es Twiteable
    print("El texto es Twiteable") # Mostramos un mensaje
else:
    print("El texto no es Twiteable")

"""
len() es una función que devuelve la longitud de un objeto. En este caso,   
devuelve el número de caracteres del texto introducido por el usuario.  
"""