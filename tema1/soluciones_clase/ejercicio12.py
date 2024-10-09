a = int(input("Introduce un número: "))
b = int(input("Introduce otro número: "))

c = "asdfg"
while c.isdigit() == False:
    c = input("Introduce otro número: ")
    if c.isdigit() == False:
        print("Por favor, introduce un número entero")

c = int(c)

if(a % 2 == 0 and b % 2 == 0) or (a % 2 == 0 and c % 2 == 0) or (b % 2 == 0 and c % 2 == 0):
    print("Dos de los números son pares")
elif a % 2 == 0 and b % 2 == 0 and c % 2 == 0: # Esta condición es redundante, no es necesario
    print("Los tres números son pares")
elif a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
    print("Al menos uno de los números es par")
elif a % 2 != 0 and b % 2 != 0 and c % 2 != 0:
    print("Los tres números son impares")
else:
    print("Al menos dos de los números son impares")