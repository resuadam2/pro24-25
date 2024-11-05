# Laboratorio 4.3.1.9: Números primos: ¿Cómo encontrarlos?

"""
Un número natural es primo si es mayor que 1 y no tiene divisores más que 1 y si mismo.

¿Complicado? De ningúna manera. Por ejemplo, 8 no es un número primo, ya que puedes dividirlo entre 2 y 4 (no podemos usar divisores iguales a 1 y 8, ya que la definición lo prohíbe).

Por otra parte, 7 es un número primo, ya que no podemos encontrar ningún divisor para el.


Tu tarea es escribir una función que verifique si un número es primo o no.

La función:

Se llama is_prime.
Toma un argumento (el valor a verificar).
Devuelve True si el argumento es un número primo, y False de lo contrario.
Sugerencia: intenta dividir el argumento por todos los valores posteriores (comenzando desde 2) y verifica el resto: si es cero, tu número no puede ser un número primo; analiza cuidadosamente cuándo deberías detener el proceso.

Si necesitas conocer la raíz cuadrada de cualquier valor, puedes utilizar el operador **. Recuerda: la raíz cuadrada de x es lo mismo que x0.5.

Complementa el código en el editor.

Ejecuta tu código y verifica si tu salida es la misma que la nuestra.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False # si el número es divisible por i, no es primo
    return True # si la función llega aqúi, el número es primo
    

def primos(n):
    for i in range(1, n + 1):
        if is_prime(i):
            print(i, end=" ")
    print()

primos(10)
primos(100)
primos(1000)
