def perfecto(n: int) -> bool:
    """
    Comprueba si un número es perfecto.\n
    Un número es perfecto si la suma de sus divisores propios es igual a él mismo.
    """
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    """
    if suma == n:
        return True
    else:
        return False
    """
    return suma == n

def perfectoMejorada(n: int) -> bool:
    """
    Comprueba si un número es perfecto.\n
    Un número es perfecto si la suma de sus divisores propios es igual a él mismo.
    """
    suma = sum([i for i in range(1, n//2 + 1) if n % i == 0])
    return suma == n

def comprobacionPerfectos(min: int, max: int) -> None:
    for i in range(min, max + 1):
        if perfectoMejorada(i):
            print(f"{i} es un número perfecto.")

print(perfecto(6)) # True
print(perfecto(10)) # False
print(perfecto(28)) # True

comprobacionPerfectos(1, 50000) # 6, 28, 496, 8128
