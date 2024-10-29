def suma_divisores_sin_n(n):
    suma = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            suma += i
    return suma

def suma_divisores_sin_n_mejorada(n):
    return sum([i for i in range(1, n//2 + 1) if n % i == 0])

def numeros_amigos(n, m):
    if n == m:
        return False
    elif suma_divisores_sin_n(n) == m and suma_divisores_sin_n_mejorada(m) == n:
        return True
    else:
        return False
    
# Pruebas
print(numeros_amigos(220, 284)) # True
print(numeros_amigos(1184, 1210)) # True
print(numeros_amigos(220, 220)) # False
print(numeros_amigos(220, 221)) # False
