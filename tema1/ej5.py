# Ejercicio 5
"""
Diseñar un algoritmo que lea del teclado dos números enteros
y un carácter. El caracter puede ser +, -, *, /, %, ^, y en 
función del carácter introducido se mostrará el resultado de    
la operación correspondiente. 
Por ejemplo, si se introduce '7', '3' y '+' se mostrará 10.
"""
print("Introduzca el primer número: ") # Pedimos el primer número   
num1 = int(input()) # Leemos el primer número   
print("Introduzca el segundo número: ") # Pedimos el segundo número 
num2 = int(input()) # Leemos el segundo número  
print("Introduzca el operador (+, -, *, /, %, ^): ") # Pedimos el operador  
operador = input() # Leemos el operador 
match operador: # Comprobamos el operador
    case "+": # Si el operador es suma
        print(num1 + num2) # Mostramos el resultado
    case "-": # Si el operador es resta
        print(num1 - num2) # Mostramos el resultado
    case "*": # Si el operador es multiplicación
        print(num1 * num2) # Mostramos el resultado
    case "/": # Si el operador es división
        print(num1 / num2) # Mostramos el resultado
    case "%": # Si el operador es módulo
        print(num1 % num2) # Mostramos el resultado
    case "^": # Si el operador es potencia
        print(num1 ** num2) # Mostramos el resultado
    case _:
        print("Operador no válido") # Mostramos un mensaje de error