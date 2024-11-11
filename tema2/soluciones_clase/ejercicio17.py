def leerNumeros() -> list:
    """
    Función que pide un número de números a ingresar y después pide esos números.
    Los almacena en una lista y devuelve la lista.
    """
    cantidad = int(input("¿Cuántos números quieres ingresar? "))
    numeros = []
    for i in range(cantidad):
        numeros.append(int(input(f"Ingresa el número {i + 1}: ")))
    return numeros

def leerNumerosSinCantidad() ->list:
    """
    Función que pide números hasta que se ingresa un número negativo.
    Devuelve una lista con los números ingresados.
    """
    numeros = []
    numero = int(input("Ingresa un número (negativo para terminar): "))
    while numero >= 0:
        numeros.append(numero)
        numero = int(input("Ingresa un número (negativo para terminar): "))
    return numeros

def sumaLista(lista: list) -> int:
    """
    Función que recibe una lista de números y devuelve la suma de los números.
    """
    suma = 0
    for numero in lista:
        suma += numero
    return suma

def sumaListaVagos(lista: list) -> int:
    """
    Función que recibe una lista de números y devuelve la suma de los números.
    """
    return sum(lista)

def mayorLista(lista: list) -> int:
    """
    Función que recibe una lista de números y devuelve el mayor de los números.
    """
    mayor = lista[0]
    for numero in lista:
        if numero > mayor:
            mayor = numero
    return mayor

def mayorListaVagos(lista: list) -> int:
    """
    Función que recibe una lista de números y devuelve el mayor de los números.
    """
    return max(lista)

def menorLista(lista: list) -> int:
    """
    Función que recibe una lista de números y devuelve el menor de los números.
    """
    menor = lista[0]
    for numero in lista:
        if numero < menor:
            menor = numero
    return menor

def menorListaVagos(lista: list) -> int:
    """
    Función que recibe una lista de números y devuelve el menor de los números.
    """
    return min(lista)

def promedioLista(lista: list) -> float:
    """
    Función que recibe una lista de números y devuelve el promedio de los números.
    """
    return sumaListaVagos(lista) / len(lista)

def medianaLista(lista: list) -> int:
    """
    Función que recibe una lista de números y devuelve la mediana de los números.
    """
    lista.sort()
    if len(lista) % 2 == 0:
        return (lista[len(lista) // 2 - 1] + lista[len(lista) // 2]) / 2
    return lista[len(lista) // 2]