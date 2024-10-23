# Recursividad

"""
La recursividad es un concepto muy importante en programación.
Se trata de una técnica que consiste en que una función se llame a sí misma.
"""

# Ejemplo de función recursiva

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5)) # 120

"""
En este caso, la función factorial se llama a sí misma para calcular 
el factorial de un número. La condición de parada es que si n es igual a 0, 
se devuelve 1. En caso contrario, se devuelve n multiplicado por el factorial de n-1.    

La recursividad es una técnica muy potente, pero hay que tener cuidado con ella, 
ya que si no se controla bien, puede llevar a un bucle infinito. 
Por ejemplo, si no se cumple la condición de parada, 
la función se llamará a sí misma indefinidamente.
"""

# Ejemplo de recursividad infinita

def f():
    return f() # Llamada recursiva infinita

# f() # RecursionError: maximum recursion depth exceeded

"""
En este caso, la función f se llama a sí misma indefinidamente,
lo que provoca un error de recursión. Para evitar este problema,
es importante asegurarse de que la función tenga una condición de parada
que permita salir de la recursión en algún momento.
"""

"""
La recursividad se puede utilizar para resolver una amplia variedad de problemas,
como el cálculo de factoriales, la generación de secuencias matemáticas,
la búsqueda de caminos en grafos, etc. Es una técnica muy versátil
que puede simplificar la implementación de algoritmos complejos.
"""

# Ejemplo de función recursiva para calcular la serie de Fibonacci

"""
La serie de Fibonacci es una secuencia matemática en la que cada término
es la suma de los dos términos anteriores. Los primeros términos de la serie
son 0, 1, 1, 2, 3, 5, 8, 13, 21, etc. La serie de Fibonacci se puede calcular
de forma recursiva de la siguiente manera:
"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(4)) 

"""
En este caso, la función fibonacci se llama a sí misma para calcular
el n-ésimo término de la serie de Fibonacci. La condición de parada
es que si n es igual a 0, se devuelve 0, y si n es igual a 1, se devuelve 1.
En caso contrario, se devuelve la suma de los dos términos anteriores.
"""

