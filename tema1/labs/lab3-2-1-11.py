# Laboratorio 3.2.1.10: La sentencia continue - El Bonito devorador de vocales

"""
Tu tarea aquí es aún más especial que antes: 
¡Debes rediseñar el devorador de vocales (feo) del laboratorio anterior (3.1.2.10) y 
crear un mejor devorador de vocales (bonito) mejorado! Escribe un programa que use:

Un bucle for.
El concepto de ejecución condicional (if-elif-else).
La instrucción continue.
Tu programa debe:

Pedir al usuario que ingrese una palabra.
Utilizar user_word = user_word.upper() para convertir la palabra ingresada por el usuario a mayúsculas; hablaremos sobre los llamados métodos de cadena y el upper() muy pronto, no te preocupes.
Emplea la ejecución condicional y la instrucción continue para "comer" las siguientes vocales A , E , I , O , U de la palabra ingresada.
Asigne las letras no consumidas a la variable word_without_vowels e imprime la variable en la pantalla.
Analiza el código en el editor. Hemos creado word_without_vowels y le hemos asignado una cadena vacía. Utiliza la operación de concatenación para pedirle a Python que combine las letras seleccionadas en una cadena más larga durante los siguientes giros de bucle, y asignarlo a la variable word_without_vowels.

Prueba tu programa con los datos que le proporcionamos.
"""

word_without_vowels = ""

user_word = input("Ingrese una palabra: ")

user_word = user_word.upper()

for letra in user_word:
    if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        continue
    else:
        word_without_vowels += letra
else:
    print(word_without_vowels)

# Otra opcion

# for letra in user_word:
#     if letra in "AEIOU":
#         continue
#     else:
#         print(letra, end="")