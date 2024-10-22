# Ejercicio 17

"""
Diseñar varias funciones para cumplir con los siguientes requisitos:
1. Función que lea una serie de números enteros positivos desde teclado y los almacene en una lista.
2. Función que reciba una lista de enteros y devuelva la suma de los elementos.
3. Función que reciba una lista de enteros y devuelva el mayor.
4. Función que reciba una lista de enteros y devuelva el menor.
5. Función que reciba una lista de enteros y devuelva la media.
6. Función que reciba una lista de enteros y devuelva la mediana.
7. Función que reciba una lista de enteros y devuelva la varianza.
8. Función que reciba una lista de enteros y devuelva la desviación típica.
9. función que reciba una lista de enteros y devuelva si es simétrica o no.
10. Función que reciba una lista de enteros y devuelva si cada elemento es un número primo o no.    
11. Función que reciba una lista de enteros y devuelva si cada elemento es un número capicúa o no.  
Incluir un programa que pruebe todas las funciones.
"""

def leer_lista_positivos():
    lista = []
    while True:
        numero = int(input("Introduce un número entero positivo (0 para terminar): "))
        if numero == 0:
            break
        elif numero < 0:
            print("El número debe ser positivo.")
        else:
            lista.append(numero)
    return lista    

def suma_elementos(lista):
    return sum(lista)

def mayor_elemento(lista):
    return max(lista)

def menor_elemento(lista):
    return min(lista)

def media_elementos(lista):
    return sum(lista) / len(lista)

def mediana_elementos(lista):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    if n % 2 == 0:
        return (lista_ordenada[n // 2 - 1] + lista_ordenada[n // 2]) / 2
    else:
        return lista_ordenada[n // 2]
    
def varianza_elementos(lista):
    media = media_elementos(lista)
    return sum((x - media) ** 2 for x in lista) / len(lista)

def desviacion_tipica(lista):
    return varianza_elementos(lista) ** 0.5

def simetrica(lista):
    return lista == lista[::-1]

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def primos(lista):
    return [es_primo(x) for x in lista]

def capicua(numero):
    return str(numero) == str(numero)[::-1]

def capicuas(lista):
    return [capicua(x) for x in lista]

if __name__ == "__main__":
    lista = leer_lista_positivos()
    print(f"Lista: {lista}")
    print(f"Suma: {suma_elementos(lista)}")
    print(f"Mayor: {mayor_elemento(lista)}")
    print(f"Menor: {menor_elemento(lista)}")
    print(f"Media: {media_elementos(lista)}")
    print(f"Mediana: {mediana_elementos(lista)}")
    print(f"Varianza: {varianza_elementos(lista)}")
    print(f"Desviación típica: {desviacion_tipica(lista)}")
    print(f"Simétrica: {simetrica(lista)}")
    print(f"Números primos: {primos(lista)}")
    print(f"Números capicúa: {capicuas(lista)}")


