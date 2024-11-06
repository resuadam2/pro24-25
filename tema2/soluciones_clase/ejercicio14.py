def printAsMatrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end="\t")
        print()

def printAsMatrixRangeVersion(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="\t")
        print()

if __name__ == "__main__":
    matrizEjemploA = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    printAsMatrix(matrizEjemploA)
    printAsMatrixRangeVersion(matrizEjemploA)
