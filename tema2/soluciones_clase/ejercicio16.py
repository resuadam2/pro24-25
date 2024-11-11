def esCuadrada(matrix: list) -> bool:
    """
    Función que recibe una matriz y devuelve True si es cuadrada, False en caso contrario.
    """
    filas = len(matrix)
    for fila in matrix:
        if len(fila) != filas:
            return False
    return True

def traspuesta(matrix: list) -> list:
    """
    Función que recibe una matriz y devuelve su traspuesta.
    La matriz debe ser cuadrada.
    """
    if not esCuadrada(matrix):
        return None
    traspuesta = []
    for i in range(len(matrix)):
        traspuesta.append([])
        for j in range(len(matrix)):
            traspuesta[i].append(matrix[j][i])
    return traspuesta

def esSimetrica(matrix: list) -> bool:
    """
    Función que recibe una matriz y devuelve True si es simétrica, False en caso contrario.
    """
    if not esCuadrada(matrix):
        return False
    return matrix == traspuesta(matrix)

from ejercicio14 import printAsMatrix

# Ejemplo
if __name__ == "__main__":
    matrix = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
    print(esCuadrada(matrix))  # True
    print("Original:")
    printAsMatrix(matrix)  # 4	2
    print("Traspuesta:")
    printAsMatrix(traspuesta(matrix))  # [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
    print(esSimetrica(matrix))  # True
    matrix = [[1, 2, 3], [7, 4, 5], [7, 5, 4]]
    print(esCuadrada(matrix))  # True
    print("Original:")
    printAsMatrix(matrix)  # 4	2
    print("Traspuesta:")
    printAsMatrix(traspuesta(matrix)) 
    print(esSimetrica(matrix))  # True
    matrix = [[1, 2, 3], [2, 4, 5]]
    print(esCuadrada(matrix))  # False
    print("Original:")
    printAsMatrix(matrix)  # 4	2
    print("Traspuesta:")
    print(traspuesta(matrix))  # None
    print(esSimetrica(matrix))  # False
    matrix = [[4, 2], [2, 4]]
    print(esCuadrada(matrix))  # True
    print("Original:")
    printAsMatrix(matrix)  # 4	2
    print("Traspuesta:")
    printAsMatrix(traspuesta(matrix))  # [[4, 2], [2, 4]]
    print(esSimetrica(matrix))  # True
