def max_in_lista(lista):
    maximo = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
    return maximo

def max_in_lista_sin_verguenza(lista):
    return max(lista)

def pos_max_in_lista(lista):
    maximo = lista[0]
    pos_max = 0
    for i in range(1, len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
            pos_max = i
    return pos_max

def pos_max_in_lista_sin_verguenza(lista):
    return lista.index(max(lista))

def pos_max_and_max_value_in_lista(lista):
    maximo = lista[0]
    pos_max = 0
    for i in range(1, len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
            pos_max = i
    return pos_max, maximo

def max_positions_of_the_max_value_in_lista(lista):
    maximo = lista[0]
    posiciones = [0]
    for i in range(1, len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
            posiciones = [i]
        elif lista[i] == maximo:
            posiciones.append(i)
    return posiciones


if __name__ == "__main__":
    print(max_in_lista([1, 2, 3, 4, 5]))  # 5
    print(max([1, 2, 3, 4, 5]))  # 5
    print(max_in_lista_sin_verguenza([1, 2, 3, 4, 5]))  # 5
    print(pos_max_in_lista([1, 2, 3, 4, 5]))  # 4
    print(pos_max_in_lista_sin_verguenza([1, 2, 3, 4, 5]))  # 4
    print(pos_max_and_max_value_in_lista([1, 2, 3, 4, 5]))  # (4, 5)
    print(max_positions_of_the_max_value_in_lista([1, 2, 3, 4, 5]))  # [4]
    print(max_positions_of_the_max_value_in_lista([1, 2, 3, 4, 5, 5]))  # [4, 5]
    print(max_positions_of_the_max_value_in_lista([5, 2, 3, 4, 3, 5, 5]))  # [0, 5, 6]

