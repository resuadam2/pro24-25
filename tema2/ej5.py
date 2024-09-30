# Ejercicio 5 - Usando strings

"""
Diseñar una función que invierta los dígitos de un número entero positivo (debe comprobarse que el número es positivo).
"""

def invertir_numero(numero):
    if numero < 0:
        return "El número debe ser positivo."
    else:
        return int(str(numero)[::-1])
    
if __name__ == "__main__":
    numero = int(input("Introduce un número entero positivo: "))
    print(f"El número invertido es: {invertir_numero(numero)}")