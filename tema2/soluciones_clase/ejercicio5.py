def invertir_digitos(n: int) -> int:
    if n < 0:
        print("Por favor, introduzca un número positivo")
        return -1
    toret = 0
    while n > 0:
        toret = toret * 10 + n % 10
        n = n // 10
    return toret

def invertir_digitos_v2(n: int) -> int:
    if n < 0:
        print("Por favor, introduzca un número positivo")
        return -1
    return int(str(n)[::-1])

def invertir_digitos_usando_valor_absoluto(n: int) -> int:
    return int(str(abs(n))[::-1])


# Pruebas
print(invertir_digitos(0))
print(invertir_digitos(-123))
print(invertir_digitos(1234))

print(invertir_digitos_v2(0))
print(invertir_digitos_v2(-123))
print(invertir_digitos_v2(1234))

print(invertir_digitos_usando_valor_absoluto(0))
print(invertir_digitos_usando_valor_absoluto(-123))
print(invertir_digitos_usando_valor_absoluto(1234))
