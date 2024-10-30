import math

def area_circunferencia(radio):
    return math.pi * radio ** 2

def area_cuadrado(lado):
    return lado ** 2

def area_rectangulo(base, altura):
    return base * altura

def area_triangulo_equilatero(lado):
    return (math.sqrt(3) / 4) * lado ** 2

def perimetro_circunferencia(radio):
    return 2 * math.pi * radio

def perimetro_cuadrado(lado):
    return 4 * lado

def perimetro_rectangulo(base, altura):
    return 2 * (base + altura)

def perimetro_triangulo(lado1, lado2, lado3):
    return lado1 + lado2 + lado3

def print_menu_operaciones():
    print("Operaciones con figuras geométricas")
    print("1. Circunferencia")
    print("2. Cuadrado")
    print("3. Rectángulo")
    print("4. Triángulo equilátero")
    print("0. Salir")

def seleccion_figura():
    print_menu_operaciones()
    opcion = input("Seleccione una figura: ")
    while opcion not in ["1", "2", "3", "4", "0"]:
        print("Opción no válida")
        print("\n\n")
        print_menu_operaciones()
        opcion = input("Seleccione una figura: ")
    return opcion

def calculos_figuras(opcion):
    match(opcion):
        case "1":
            radio = float(input("Ingrese el radio de la circunferencia: "))
            print(f"Área de la circunferencia: {area_circunferencia(radio)}")
            print(f"Perímetro de la circunferencia: {perimetro_circunferencia(radio)}")
        case "2":
            lado = float(input("Ingrese el lado del cuadrado: "))
            print(f"Área del cuadrado: {area_cuadrado(lado)}")
            print(f"Perímetro del cuadrado: {perimetro_cuadrado(lado)}")
        case "3":
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))
            print(f"Área del rectángulo: {area_rectangulo(base, altura)}")
            print(f"Perímetro del rectángulo: {perimetro_rectangulo(base, altura)}")
        case "4":
            lado = float(input("Ingrese el lado del triángulo: "))
            print(f"Área del triángulo equilátero: {area_triangulo_equilatero(lado)}")
            print(f"Perímetro del triángulo equilátero: {perimetro_triangulo(lado, lado, lado)}")

def main():
    opcion = seleccion_figura()
    while opcion != "0":
        calculos_figuras(opcion)
        opcion = seleccion_figura()
    print("Hasta luego")

if __name__ == "__main__":
    main()
    
