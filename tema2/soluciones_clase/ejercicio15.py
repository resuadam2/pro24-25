def matrixProduct(matrixA, matrixB) -> list:
    if len(matrixA[0]) != len(matrixB):
        return None
    matrixProduct = []
    for i in range(len(matrixA)):
        row = []
        for j in range(len(matrixB[0])):
            product = 0
            for k in range(len(matrixA[i])):
                product += matrixA[i][k] * matrixB[k][j]
            row.append(product)
        matrixProduct.append(row)
    return matrixProduct

from ejercicio14 import printAsMatrix

if __name__ == "__main__":
    matrizEjemploA = [[0,1], [1,0]]
    matrizEjemploB = [[2,3], [4,5]]
    printAsMatrix(matrizEjemploA)  # 1	2	3
    print("x")
    printAsMatrix(matrizEjemploB)  # 9	8	7
    print("=")
    printAsMatrix(matrixProduct(matrizEjemploA, matrizEjemploB))  # [[30, 24, 18], [84, 69, 54], [138, 114, 90]]    