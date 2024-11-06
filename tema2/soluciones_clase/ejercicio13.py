def matricesMismaDimension(matrizA, matrizB) -> bool:
    if len(matrizA) != len(matrizB):
        return False
    for i in range(len(matrizA)):
        if len(matrizA[i]) != len(matrizB[i]):
            return False
    return True

def sumaMatrices(matrizA, matrizB) -> list:
    if not matricesMismaDimension(matrizA, matrizB):
        return None
    matrizSuma = []
    for i in range(len(matrizA)):
        fila = []
        for j in range(len(matrizA[i])):
            fila.append(matrizA[i][j] + matrizB[i][j])
        matrizSuma.append(fila)
    return matrizSuma

from ejercicio14 import printAsMatrix

if __name__ == "__main__":
    matrizEjemploA = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrizEjemploB = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    printAsMatrix(matrizEjemploA)  # 1	2	3
    print("+")
    printAsMatrix(matrizEjemploB)  # 9	8	7
    print("=")
    printAsMatrix(sumaMatrices(matrizEjemploA, matrizEjemploB))  # [[10, 10, 10], [10, 10, 10], [10, 10, 10]]
    matrizEjemploC = [[1, 2, 3], [4, 5, 6], [7, 8]]
    matrizEjemploD = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    print(sumaMatrices(matrizEjemploC, matrizEjemploD))  # None