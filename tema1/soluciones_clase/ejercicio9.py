sum = 0

for i in range(1, 501):
    if i % 5 == 0 and i % 7 == 0:
        sum += i

print(f"La suma de los números entre 1 y 500 que son múltiplos de 5 y 7 es {sum}")