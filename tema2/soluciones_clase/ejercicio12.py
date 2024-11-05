def invierte_lista(lista):
    return lista[::-1]

def invierte_lista_sin_verguenza(lista):
    return list(reversed(lista))

def invierte_lista_recorriendola(lista):
    lista_invertida = []
    for i in range(len(lista) - 1, -1, -1):
        lista_invertida.append(lista[i])
    return lista_invertida

if __name__ == "__main__":
    print(invierte_lista([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]
    print(invierte_lista_sin_verguenza([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]
    print(invierte_lista_recorriendola([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]