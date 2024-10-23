

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
def numPerfecto(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma == n

def numPrimo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

