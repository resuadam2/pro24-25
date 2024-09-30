# Ejercicio 10

"""
Realiza un programa que tenga varias funciones para calcular el área y el perímetro de circunferencias, rectángulos, 
cuadrados y triángulos equiláteros.
El cuerpo del programa debe probar todas las funciones.
"""

import math

def area_circunferencia(radio):
    return math.pi * radio ** 2

def perimetro_circunferencia(radio):
    return 2 * math.pi * radio

def area_rectangulo(base, altura):
    return base * altura

def perimetro_rectangulo(base, altura):
    return 2 * (base + altura)

def area_cuadrado(lado):
    return lado ** 2

def perimetro_cuadrado(lado):
    return 4 * lado

def area_triangulo_equilatero(lado):
    return (math.sqrt(3) / 4) * lado ** 2

def perimetro_triangulo_equilatero(lado):
    return 3 * lado

if __name__ == "__main__":
    radio = 5
    base = 4
    altura = 3
    lado = 6

    print(f"El área de la circunferencia de radio {radio} es: {area_circunferencia(radio)}")
    print(f"El perímetro de la circunferencia de radio {radio} es: {perimetro_circunferencia(radio)}")
    print(f"El área del rectángulo de base {base} y altura {altura} es: {area_rectangulo(base, altura)}")
    print(f"El perímetro del rectángulo de base {base} y altura {altura} es: {perimetro_rectangulo(base, altura)}")
    print(f"El área del cuadrado de lado {lado} es: {area_cuadrado(lado)}")
    print(f"El perímetro del cuadrado de lado {lado} es: {perimetro_cuadrado(lado)}")
    print(f"El área del triángulo equilátero de lado {lado} es: {area_triangulo_equilatero(lado)}")
    print(f"El perímetro del triángulo equilátero de lado {lado} es: {perimetro_triangulo_equilatero(lado)}")