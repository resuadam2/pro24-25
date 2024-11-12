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

def medianaLista(lista: list) -> float:
    """
    Función que recibe una lista de números y devuelve la mediana de los números.
    """
    lista.sort()
    if len(lista) % 2 == 0:
        return (lista[len(lista) // 2 - 1] + lista[len(lista) // 2]) / 2
    return lista[len(lista) // 2]

def varianzaLista(lista: list) -> float:
    """
    Función que recibe una lista de números y devuelve la varianza de los números.
    """
    promedio = promedioLista(lista)
    suma = 0
    for numero in lista:
        suma += (numero - promedio) ** 2
    return suma / len(lista)

# Probar más adelante si hace falta restarle 1 al resultado de la varianza

def desviacionEstandarLista(lista: list) -> float:
    """
    Función que recibe una lista de números y devuelve la desviación estándar de los números.
    """
    return varianzaLista(lista) ** 0.5

def esSimetrica(lista: list) -> bool:
    """
    Función que recibe una lista de números y devuelve True si es simétrica, False si no lo es.
    """
    return lista == lista[::-1]

def esSimetricaSinSlicing(lista: list) -> bool:
    """
    Función que recibe una lista de números y devuelve True si es simétrica, False si no lo es.
    """
    for i in range(len(lista) // 2):
        if lista[i] != lista[len(lista) - 1 - i]:
            return False
    return True

def esPrimo(numero: int) -> bool:
    """
    Función que recibe un número y devuelve True si es primo, False si no lo es.
    """
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def primosLista(lista: list) -> list:
    """
    Función que recibe una lista de números y devuelve una lista con los números primos.
    """
    primos = []
    for numero in lista:
        if esPrimo(numero):
            primos.append(numero)
    return primos

def esPrimoLista(lista: list) -> list:
    """
    Función que recibe una lista de números y devuelve una lista con True si es primo y False si no lo es.
    """
    primos = []
    for numero in lista:
        primos.append(esPrimo(numero))
    return primos

def esPrimoListaPorCompresion(lista: list) -> list:
    """
    Función que recibe una lista de números y devuelve una lista con True si es primo y False si no lo es.
    """
    return [esPrimo(numero) for numero in lista]

def esCapicua(numero: int) -> bool:
    """
    Función que recibe un número y devuelve True si es capicúa, False si no lo es.
    """
    return str(numero) == str(numero)[::-1]

def capicuasLista(lista: list) -> list:
    """
    Función que recibe una lista de números y devuelve una lista con los números capicúa.
    """
    capicuas = []
    for numero in lista:
        if esCapicua(numero):
            capicuas.append(numero)
    return capicuas

def esCapicuaLista(lista: list) -> list:
    """
    Función que recibe una lista de números y devuelve una lista con True si es capicúa y False si no lo es.
    """
    capicuas = []
    for numero in lista:
        capicuas.append(esCapicua(numero))
    return capicuas

def esCapicuaListaPorCompresion(lista: list) -> list:
    """
    Función que recibe una lista de números y devuelve una lista con True si es capicúa y False si no lo es.
    """
    return [esCapicua(numero) for numero in lista]

def main():
    numeros = leerNumeros()
    print(f"La suma de los números es {sumaListaVagos(numeros)}")
    print(f"El mayor número es {mayorListaVagos(numeros)}")
    print(f"El menor número es {menorListaVagos(numeros)}")
    print(f"El promedio de los números es {promedioLista(numeros)}")
    print(f"La mediana de los números es {medianaLista(numeros)}")
    print(f"La varianza de los números es {varianzaLista(numeros)}")
    print(f"La desviación estándar de los números es {desviacionEstandarLista(numeros)}")
    print(f"¿Es simétrica la lista? {esSimetrica(numeros)}")
    primos = primosLista(numeros)
    print(f"Los números primos de la lista son {primos}")
    print(f"¿Es primo cada número de la lista? {esPrimoLista(numeros)}")
    capicuas = capicuasLista(numeros)
    print(f"Los números capicúa de la lista son {capicuas}")
    print(f"¿Es capicúa cada número de la lista? {esCapicuaLista(numeros)}")


if __name__ == "__main__":
    main()