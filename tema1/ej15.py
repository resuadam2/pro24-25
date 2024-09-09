# Ejercicio 15
"""
Diseñar un algoritmo que lea una secuencia de 20
números reales introducidos por teclado. Al acabar
la secuencia, debe mostrar el valor máximo y mínimo 
introdcidos.
"""
# Pedimos los números
maximo = float("-inf") # Inicializamos el máximo
minimo = float("inf") # Inicializamos el mínimo
for x in range(20): # Bucle para leer los 20 números
    print("Introduzca un número real: ") # Pedimos un número real
    numero = float(input()) # Leemos un número
    if numero > maximo: # Si el número es mayor que el máximo
        maximo = numero # Actualizamos el máximo
    if numero < minimo: # Si el número es menor que el mínimo
        minimo = numero # Actualizamos el mínimo
print("El máximo es ", maximo) # Mostramos el máximo
print("El mínimo es ", minimo) # Mostramos el mínimo

"""
float("-inf") es un número muy pequeño y float("inf") es un número muy grande.  
Por lo tanto, al principio, cualquier número que se introduzca será mayor que el máximo y menor que el mínimo.  
En otros lenguajes de programación, se puede utilizar None para inicializar el máximo y el mínimo.  
También se puede utilizar un booleano para saber si es la primera vez que se introduce un número.   
Otra opción sería inicializar el máximo y el mínimo al primer número introducido.   
"""