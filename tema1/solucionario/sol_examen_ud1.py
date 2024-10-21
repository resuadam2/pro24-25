# Resuelve los siguientes ejercicios sin modificar ninguna de las lineas de código existentes.
# Nota: no se pueden modificar las líneas pero si se pueden añadir líneas de código entre las de inicio y final si se necesita más espacio.

# Ejericio 1 (2 puntos)

"""
Diseña un algoritmo que calcule la cantidad de propinas que se deben dar en un restaurante.
El algoritmo debe leer de teclado el total de la cuenta y preguntarle al usuario si su servicio fue bueno, malo o regular.
Para saber la opción elegida por el usuario, se debe indicar que el usuario debe escribir "bueno", "malo" o "regular",
 puede escribirlo en minúsculas, mayúsculas o combinando ambas y debe funcionar igual.   
En caso de que el servicio haya sido bueno, el algoritmo debe calcular el 20% del total de la cuenta.   
En caso de que el servicio haya sido regular, el algoritmo debe calcular el 15% del total de la cuenta.
En caso de que el servicio haya sido malo, el algoritmo debe calcular el 10% del total de la cuenta.
Finalmente, el algoritmo debe imprimir el total de la cuenta más la propina y el total de la propina, por separado.   
"""

print("Ejercicio 1 - Calculadora de propinas")

total_cuenta = float(input("Introduce el total de la cuenta: "))
valida = False

while not valida:
    servicio = input("¿Cómo ha sido el servicio? (bueno, malo, regular): ").lower()
    if servicio == "bueno" or servicio == "malo" or servicio == "regular":
        valida = True
    else:
        print("Opción no válida")

if servicio == "bueno":
    propina = total_cuenta * 0.20
elif servicio == "regular":
    propina = total_cuenta * 0.15
elif servicio == "malo":
    propina = total_cuenta * 0.10

print("El total de la cuenta es:", (total_cuenta + propina), "€ y la propina es: ", propina, "€.")

print("-"*20)

# Ejericio 2 (2 puntos)


"""
Diseñar un algoritmo que nos diga si la palabra introducida por el usuario es un palíndromo o no.   
Un palíndromo es una palabra que se lee igual de izquierda a derecha que de derecha a izquierda.    
Por ejemplo, la palabra "oso" es un palíndromo.
El algoritmo debe leer una palabra del usuario y comprobar si es un palíndromo o no.
"""
print("Ejercicio 2 - Comprobador de palíndromos")

# Versión sin bucles

palabra = input("Introduce una palabra: ")

palabra = palabra.lower()

if palabra == palabra[::-1]: # [::-1] invierte la cadena
    print("La palabra", palabra, "es un palíndromo.")
else:
    print("La palabra", palabra, "no es un palíndromo.")

print("-"*20)

# Versión con bucles

palabra = input("Introduce una palabra: ")

palabra = palabra.lower()

es_palindromo = True

for i in range(len(palabra)//2):
    if palabra[i] != palabra[-i-1]:
        es_palindromo = False
        break

if es_palindromo:
    print("La palabra", palabra, "es un palíndromo.")
else:
    print("La palabra", palabra, "no es un palíndromo.")


# Ejericio 3 (2 puntos)

"""
Diseñar un algoritmo que calcule la edad de una persona en función de su fecha de nacimiento.
El algoritmo debe leer el año, mes y día de nacimiento de la persona y calcular su edad a día de hoy.
Hay que comprobar que la fecha de nacimiento es válida, aunque se da por hecho que los datos introducidos
 por el usuario serán números enteros.
Finalmente, el algoritmo debe imprimir la edad de la persona.
"""

print("Ejercicio 3 - Calculadora de edad")

anio_actual = 2024
mes_actual = 10
dia_actual = 16

fecha_valida = False

while not fecha_valida:
    anio_nacimiento = int(input("Introduce el año de nacimiento: "))
    mes_nacimiento = int(input("Introduce el mes de nacimiento: "))
    dia_nacimiento = int(input("Introduce el día de nacimiento: "))
    if mes_nacimiento >= 1 and mes_nacimiento <= 12 and dia_nacimiento >= 1 and dia_nacimiento <= 31 and anio_nacimiento <= anio_actual:    
        fecha_valida = True
    else:
        print("Fecha no válida")

if mes_actual < mes_nacimiento or (mes_actual == mes_nacimiento and dia_actual < dia_nacimiento):
    edad = anio_actual - anio_nacimiento - 1
else:
    edad = anio_actual - anio_nacimiento

print("La edad de la persona es:", edad, "años")

print("-"*20)

# Ejericio 4 (2 puntos)

"""
Diseña un algoritmo que pinte por pantalla un rombo hueco con asteriscos.
El programa debe pedir la altura del rombo al usuario y pintar el rombo con esa altura.
Se debe comprobar que la altura mínima es igual o mayor a 3, y además, que la altura es un número impar.    
En caso de que no se cumplan los requisitos, el programa debe imprimir un mensaje de error y volver a pedir el dato al usuario. 
"""

# Ejemplo de salida para una altura de 5:
#   *
#  * *
# *   *
#  * *
#   *

print("Ejercicio 4 - Rombo hueco")

altura = int(input("Introduce la altura del rombo: "))
if altura < 3 or altura % 2 == 0:
    print("Altura no válida")
else:
    for i in range(altura):
        if i < altura//2:
            espacios = " "*(altura//2 - i)
            if i == 0:
                print(espacios + "*")
            else:
                print(espacios + "*" + " "*(2*i-1) + "*")
        elif i == altura//2:
            print("*" + " "*(altura-2) + "*")
        elif i == altura-1:
            print(" "*(altura//2) + "*")
        else:
            espacios = " "*(i-altura//2)
            print(espacios + "*" + " "*(2*(altura-i)-3) + "*")

print("-"*20)

# Ejericio 5 (2 puntos - 1 punto cada versión - Jugando con los dígitos) 

"""
Diseñar un algoritmo que pida al usuario un número entero y calcule la suma de los dígitos de ese número.
Una vez tenga la suma calculada debe dividir el resultado entre el total de dígitos que tiene el número.
Finalmente, el algoritmo debe imprimir el resultado de la división.
Hay que controlar el que el número introducido por el usuario sea positivo.
Este ejercicio hay que resolverlo de dos maneras, es decir, debes hacer dos versiones del algoritmo:
Una con un bucle while y con un bucle for. Cada versión debe tener su propio código y no se pueden mezclar.
Cada versión del algoritmo tendrá un valor de 1 punto.
"""

print("Ejercicio 5 - Jugando con los dígitos - versión while")

numero = int(input("Introduce un número entero positivo: "))

if numero < 0: 
    print("Número no válido")
else:
    suma = 0
    contador = 0
    while numero > 0:
        suma += numero % 10
        numero = numero // 10
        contador += 1

    print("El resultado de la división es:", suma/contador)

print("-"*20)

print("Ejercicio 5 - Jugando con los dígitos - versión for")

numero = int(input("Introduce un número entero positivo: "))
if numero < 0:
    print("Número no válido")
else:
    suma = 0
    contador = 0
    for digito in str(numero):
        suma += int(digito)
        contador += 1

    print("El resultado de la división es:", suma/contador)

print("-"*20)