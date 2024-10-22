print("Ejercicio 1")

def intercambio(a: int, b: int) -> tuple:
    """
    Intercambia los valores de a y b.
    """
    a, b = b, a
    return a, b

def intercambioMasVago(a: int, b: int) -> tuple:
    """
    Intercambia los valores de a y b.
    """
    return b, a

def intercambioGlobalSinTuplas() -> None:
    """
    Intercambia los valores de x y y.
    """
    global y
    global x
    aux = x
    x = y
    y = aux

a = 5
b = 10
print(a,b)
a,b = intercambioMasVago(a,b)
print(a,b)
x = 5
y = 10
print(x,y)
intercambioGlobalSinTuplas()
print(x,y)


