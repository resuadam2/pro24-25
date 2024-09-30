# Ejercicio 5b - Invertir número sin usar strings

"""
Diseñar una función que invierta los dígitos de un número entero positivo (debe comprobarse que el número es positivo).
"""

# Compare this snippet from tema2/ej5.py:
# Esta vez sin usar strings, sino operaciones matemáticas.
def invertir_numero(numero):
    if numero < 0:
        return "El número debe ser positivo."
    else:
        invertido = 0
        while numero > 0:
            invertido = invertido * 10 + numero % 10
            numero = numero // 10
        return invertido
    
if __name__ == "__main__":
    numero = int(input("Introduce un número entero positivo: "))
    print(f"El número invertido es: {invertir_numero(numero)}")