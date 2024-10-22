# La función main

# La función main es una función que se encarga de ejecutar el código principal de un programa.
# En Python, la función main se suele definir en un bloque condicional if __name__ == "__main__":.
# En este bloque, se suelen realizar las llamadas a las funciones que se han definido en el programa.
# La función main es útil para organizar el código de un programa y para separar la lógica de la interfaz.
# Ejemplo de función main en Python:

# def main():
#     print("Hola, mundo!")
#
# if __name__ == "__main__":
#     main()
# En este ejemplo, la función main se encarga de imprimir un mensaje por pantalla.

# Al ejecutar el programa, se comprueba si el nombre del módulo es "__main__" y, en caso afirmativo, se llama a la función main.

# La función main es una convención en Python y se utiliza para indicar cuál es la función principal de un programa.

# La función main es opcional, pero es una buena práctica de programación utilizarla para organizar el código de un programa.

# La función main se puede llamar de cualquier manera, pero se suele utilizar el nombre main por convención.

# Ejemplo de uso:

def saludar(nombre):
    print(f"Hola, {nombre}!")

import sys

def hello_world():
    print(f"Hola, {sys.argv[0]}!")


if __name__ == "__main__":
    hello_world()
    saludar("Juan")

