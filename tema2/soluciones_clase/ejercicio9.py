def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "No se puede dividir por 0"
    return a / b

def division_entera(a, b):
    if b == 0:
        return "No se puede dividir por 0"
    return a // b

def modulo(a, b):
    if b == 0:
        return "No se puede dividir por 0"
    return a % b

def potencia(a, b):
    return a ** b

def raiz_cuadrada(a):
    return a ** 0.5

def numero_transformado(n: str) -> int:
    n = n.lower()
    match(n):
        case "0" | "cero":
            return 0
        case "1" | "uno":
            return 1
        case "2" | "dos":
            return 2
        case "3" | "tres":
            return 3
        case "4" | "cuatro":
            return 4
        case "5" | "cinco":
            return 5
        case "6" | "seis":
            return 6
        case "7" | "siete":
            return 7
        case "8" | "ocho":
            return 8
        case "9" | "nueve":
            return 9
        case _:
            return -1
        
def numero_correcto(n: str) -> bool:
    return numero_transformado(n) != -1



def operacion(operador, a: int, b: int = 0):
    """
    Operacion es una función que recibe un operador y dos números y devuelve el resultado de la operación correspondiente.
    Si el operador es "V", se calcula la raíz cuadrada del primer número. 
    Si el operador no es válido, se devuelve "Operador no válido".
    Para las operaciones unarias, se puede ingresar un solo número.
    """
    match(operador):
        case "+":
            return suma(a, b)
        case "-":
            return resta(a, b)
        case "*":
            return multiplicacion(a, b)
        case "/":
            return division(a, b)
        case "//":
            return division_entera(a, b)
        case "%":
            return modulo(a, b)
        case "**":
            return potencia(a, b)
        case "V":
            return raiz_cuadrada(a)
        case _:
            return "Operador no válido"
        
def operador_valido(operador: str) -> bool:
    return operador in ["+", "-", "*", "/", "//", "%", "**", "V"]
        
def print_menu():
    print("Menú de opciones - calculadora")
    print("+ -> Suma")
    print("- -> Resta")
    print("* -> Multiplicación")
    print("/ -> División")
    print("// -> División entera")
    print("% -> Módulo")
    print("** -> Potencia")
    print("V -> Raíz cuadrada")
    print("exit -> Salir")

def calculadora():
    print_menu()
    operador = input("Ingrese el operador deseado: ")
    while operador != "exit":
        if not operador_valido(operador):
            print("Operador no válido")
            print_menu()
            operador = input("Ingrese el operador deseado: ")
            continue
        if operador == "V":
            a = input("Ingrese el número: ")
            while not numero_correcto(a):
                print("Número no válido")
                a = input("Ingrese el número: ")
            print(operacion(operador, numero_transformado(a)))
        else:
            a = input("Ingrese el primer número: ")
            b = input("Ingrese el segundo número: ")
            while not numero_correcto(a) or not numero_correcto(b):
                print("Número no válido")
                a = input("Ingrese el primer número: ")
                b = input("Ingrese el segundo número: ")
            print(operacion(operador, numero_transformado(a), numero_transformado(b)))
        print_menu()
        operador = input("Ingrese el operador deseado: ")
    print("Hasta luego")

if __name__ == "__main__":
    calculadora()

