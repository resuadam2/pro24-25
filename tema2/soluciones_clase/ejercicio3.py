def factorial(n: int) -> int:
    if n < 0:
        raise None
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
def numero_de_euler(precision: int) -> float:
    return sum([1 / factorial(i) for i in range(precision)])

def numero_de_euler_simple(precision: int) -> float:
    e = 1
    n = 1
    while n < precision:
        e += 1 / factorial(n)
        n += 1
    return e

def numero_de_euler_for(precision):
    e = 1
    for n in range(1, precision):
        e += 1 / factorial(n)
    return e

def numero_de_euler_recursive(precision):
    if precision == 0:
        return 1
    else:
        return 1 / factorial(precision) + numero_de_euler_recursive(precision - 1)

import math

def numero_de_euler_factorial_math(precision):
    e = 1
    for n in range(1, precision):
        e += 1 / math.factorial(n)
    return e

def numero_de_euler_para_vagos():
    return math.e

if __name__ == "__main__":
    print("Ejercicio 3")
    print(numero_de_euler(3))  # 2.7182818011463845
    print(numero_de_euler_simple(7))  # 2.7182818011463845
    print(numero_de_euler_for(10))  # 2.7182818011463845
    print(numero_de_euler_factorial_math(500))  # 2.7182818011463845
    print(numero_de_euler_para_vagos())  # 2.718281828459045
    print(numero_de_euler_recursive(10))  # 2.7182818011463845