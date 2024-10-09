# Ejercicio 5
"""
Diseñar un algoritmo que lea del teclado dos números enteros
y un carácter. El caracter puede ser +, -, *, /, %, ^, y en 
función del carácter introducido se mostrará el resultado de    
la operación correspondiente. 
Por ejemplo, si se introduce '7', '3' y '+' se mostrará 10.
"""
print("Ingrese el primer número")
num1 = int(input())
print("Ingrese el segundo número")
num2 = int(input())
print("Ingrese el operador (+, -, *, /, %, ^)")
operador = input()
match operador:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        if num2 == 0:
            print("No se puede dividir por 0")
        else:
            print(num1 / num2)
    case "%":
        if num2 == 0:
            print("No se puede dividir por 0")
        else:
            print(num1 % num2)
    case "^":
        print(num1 ** num2)
    case _:
        print("Operador no válido")