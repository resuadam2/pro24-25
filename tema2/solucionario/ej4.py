# Ejercicio 4

"""
Diseñar una función que admita, como parámetro de entrada, un caracter y que devuelva, como salida, 
el número de veces que aparece dicho carácter en una secuencia de caracteres leída de teclado.
La secuencia de caracteres finalizará cuando el usuario introduzca un punto.
"""

def contar_caracter(caracter):
    contador = 0
    secuencia = input("Introduce una secuencia de caracteres (Use un único '.' para finalizar): ")
    while secuencia != ".":
        for c in secuencia:
            if c == caracter:
                contador += 1
        secuencia = input("Siga introduciendo caracteres (Use un único '.' para finalizar): ")
    return contador


if __name__ == "__main__":
    caracter = input("Introduce un caracter a contear: ")
    print(f"El caracter {caracter} aparece {contar_caracter(caracter)} veces en las secuencias de caracteres introducida.")

