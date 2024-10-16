# Ejercicio 9

"""
Desarrollar un programa que permita realizar sumas, restas, multiplicaciones y divisiones de dos números enteros.
Los números solo se admitirán del 0 al 9.
El programa debe incluir las siguientes especificaciones:
- Una función para cada operación.
- Una función para comprobar que los números son correctos. Se admitirán números del 0 al 9. 
Introducidos como números o como cadenas (independientemente de que sean mayúsculas o minúsculas).
La función debe convertir a entero los números introducidos como cadenas.
- Una función para mostrar el menú de operaciones.
- Un algoritmo principal que realice la llamada a las funciones.
El programa debe controlar los posibles errores del usuario al introducir datos y volver a pedir los datos si es necesario.
"""

def comprobar_numero(numero):
    numero = numero.lower()
    match numero:
        case "0" | "cero":
            return 0
        case "1" | "uno":
            return 1
        case "2" | "dos":
            return 2
        case "3" | "tres":
            return 3
        case "4" | "cuatro":
            return 4
        case "5" | "cinco":
            return 5
        case "6" | "seis":
            return 6
        case "7" | "siete":
            return 7
        case "8" | "ocho":
            return 8
        case "9" | "nueve":
            return 9
        case _:
            return None

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

def menu():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

if __name__ == "__main__":
    while True:
        menu()
        opcion = input("Introduce una opción: ")
        if opcion == "5":
            break
        numero1 = input("Introduce el primer número: ")
        numero2 = input("Introduce el segundo número: ")
        numero1 = comprobar_numero(numero1)
        numero2 = comprobar_numero(numero2)
        if numero1 is None or numero2 is None:
            print("Los números introducidos no son correctos.")
            continue
        if opcion == "1":
            print(f"La suma de {numero1} y {numero2} es: {suma(numero1, numero2)}")
        elif opcion == "2":
            print(f"La resta de {numero1} y {numero2} es: {resta(numero1, numero2)}")
        elif opcion == "3":
            print(f"La multiplicación de {numero1} y {numero2} es: {multiplicacion(numero1, numero2)}")
        elif opcion == "4":
            if numero2 == 0:
                print("No se puede dividir entre 0.")
                continue
            print(f"La división de {numero1} y {numero2} es: {division(numero1, numero2)}")
        else:
            print("Opción no válida.")