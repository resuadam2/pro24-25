print("Ejercicio 2")

def mayor_de_tres(a: int, b: int, c: int) -> int:
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(mayor_de_tres(1, 2, 3))  # 3
x = 9
y = 3
z = 6
print(mayor_de_tres(b = z, c = 0, a = y))