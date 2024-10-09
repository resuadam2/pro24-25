"""
Diseñar un algoritmo que pida una nota (valor entero) por teclado y 
dependiendo de su valor visualice la nota en letras. 
Por ejemplo, si nota es igual a 7 tiene que mostrar el texto "Notable".
"""
nota = input("Ingrese una nota (0-10): ")
match nota:
    case nota if nota <= 4:
        print("Insuficiente")
    case 5:
        print("Suficiente")
    case 6:
        print("Bien")
    case 7 | 8:
        print("Notable")
    case 9 | 10:
        print("Sobresaliente")
    case _:
        print("Nota incorrecta")
print("Fin del programa")