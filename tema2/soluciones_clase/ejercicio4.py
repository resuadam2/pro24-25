
def caracter_en_secuencia(caracter: str) -> int:
    mensaje = "Ingrese un caracter:\n(solo se leerá el primero introducido)\nPara parar introduzca un punto (.)"
    print(mensaje)
    actual = input()[0]
    contador = 0
    while actual != ".":
        if actual == caracter:
            contador += 1
        print(mensaje)
        actual = input()[0]
    return contador

# En esta versión solo vamos a contar si me introducen exactamente solo ese caracter
def caracter_en_secuencia_version_2(caracter: str) -> int:
    mensaje = "Ingrese un caracter:\nSolo se tendrá en cuenta si introduce un único caracter\nPara parar introduzca un punto (.)"
    print(mensaje)
    actual = ""
    while len(actual) != 1:
        actual = input()
        if len(actual) != 1:
            print("Por favor, introduzca un único caracter, esta entrada no se tendrá en cuenta")
    contador = 0
    while actual != ".":
        if actual == caracter:
            contador += 1
        print(mensaje)
        actual = ""
        while len(actual) != 1:
            actual = input()
            if len(actual) != 1:
                print("Por favor, introduzca un único caracter, esta entrada no se tendrá en cuenta")
    return contador

def caracter_en_secuencia_version_3(caracter: str) -> int:
    mensaje = "Ingrese un caracter o caracteres:\nPara parar introduzca un único punto (.)"
    print(mensaje)
    actual = input()
    contador = 0
    while actual != ".":
        for letra in actual:
            if letra == caracter:
                contador += 1
        print(mensaje)
        actual = input()
    return contador

def caracter_en_secuencia_version_4(caracter: str, secuencia: str) -> int:
    contador = 0
    for letra in secuencia:
        if letra == caracter:
            contador += 1
    return contador 

# Pruebas
print(caracter_en_secuencia("a"))
print(caracter_en_secuencia_version_2("a"))
print(caracter_en_secuencia_version_3("a"))
print(caracter_en_secuencia_version_4("a", "aabbccdd"))