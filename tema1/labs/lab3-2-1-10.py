# Laboratorio 3.2.1.10: La sentencia continue - El feo devorador de vocales

"""
La sentencia continue se usa para omitir el bloque actual y avanzar a la siguiente 
iteración, sin ejecutar las sentencias dentro del bucle.

Se puede usar tanto con while y for.

Tu tarea aquí es muy especial: ¡Debes diseñar un devorador de vocales! 
Escribe un programa que use:

Un bucle for.
El concepto de ejecución condicional (if-elif-else).
La sentencia continue.
Tu programa debe:

Pedir al usuario que ingrese una palabra.
Utiliza user_word = user_word.upper() para convertir la palabra ingresada por el usuario 
a mayúsculas; hablaremos sobre los llamados métodos de cadena y el upper() muy pronto, 
no te preocupes.
Utiliza la ejecución condicional y la instrucción continue para "comer" las siguientes 
vocales A , E , I , O , U de la palabra ingresada.
Imprime las letras no consumidas en la pantalla, cada una de ellas en una línea separada.
Prueba tu programa con los datos que le proporcionamos.
"""

palabra = input("Ingrese una palabra: ")

user_word = palabra.upper()

for letra in user_word:
    if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        continue
    else:
        print(letra)

# Otra opcion
# for letra in user_word:
#     if letra == "A":
#         continue
#     elif letra == "E":
#         continue
#     elif letra == "I":
#         continue
#     elif letra == "O":
#         continue
#     elif letra == "U":
#         continue
#     else:
#         print(letra)

# Otra opcion

# for letra in user_word:
#     if letra in "AEIOU":
#         continue
#     else:
#         print(letra)
