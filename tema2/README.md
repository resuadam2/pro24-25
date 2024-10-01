# Tema 1 - Algoritmos y estructuras de datos

## Apuntes y ejemplos

- [Funciones en python](funciones.py)
- [La función main](funcion_main.py)

## Enunciados ejercicios

### Ejercicio 1

Disear una función que intercambie el valor de dos variables de tipo entero. 
Incluir el algoritmo principal que realice la llamada a dicha función.

### Ejercicio 2

Diseñar una función que dado un número entero positivo, diga si es o no un número perfecto.
Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos.
Por ejemplo, 6 es perfecto porque sus divisores propios son 1, 2 y 3, que suman 6.
Incluir el algoritmo principal que realice la llamada a dicha función.

### Ejercicio 3

Diseñar una función que permita calcular el número e, o número de Euler, mediante la siguiente serie infinita:
e = 1 + 1/1! + 1/2! + 1/3! + 1/4! + ...
para una precisión dada por el usuario, la precisión indicará las vueltas que debe dar el algoritmo a la 
serie infinita. Incluir el algoritmo principal que realice la llamada a dicha función.
Como paso previo, se puede diseñar una función que calcule el factorial de un número entero.

### Ejercicio 4

Diseñar una función que admita, como parámetro de entrada, un caracter y que devuelva, como salida, 
el número de veces que aparece dicho carácter en una secuencia de caracteres leída de teclado.
La secuencia de caracteres finalizará cuando el usuario introduzca un punto.

### Ejercicio 5

Diseñar una función que invierta los dígitos de un número entero positivo (debe comprobarse que el número es positivo).

### Ejercicio 6

Diseñar una función que decida si dos números enteros positivos son amigos.
Dos números son amigos si la suma de los divisores propios de uno es igual al otro número y viceversa.
Por ejemplo, los divisores propios de 220 son 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 y 110, que suman 284.
Los divisores propios de 284 son 1, 2, 4, 71 y 142, que suman 220.
Incluir el algoritmo principal que realice la llamada a dicha función.

### Ejercicio 7

Diseñar una función que dado un número entero positivo, diga si es o no un número perfecto.
Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos.
Por ejemplo, 6 es perfecto porque sus divisores propios son 1, 2 y 3, que suman 6.
Incluir el algoritmo principal que realice la llamada a dicha función.

### Ejercicio 8

Implementar un programa de registro y login de usuarios. En primer lugar se ejecutará el código de registro,
que solicitará un nombre de usuario y una contraseña. A continuación, se ejecutará el código de login, que solicitará
el nombre de usuario y la contraseña. Si el nombre de usuario y la contraseña coinciden con los introducidos en el
registro, se mostrará un mensaje de bienvenida. En caso contrario, se mostrará un mensaje de error.
Necesitaremos una función para el registro y otra para el login.
Y las llamadas a las funciones de registro y login se realizarán en el algoritmo principal.

### Ejercicio 9

Desarrollar un programa que permita realizar sumas, restas, multiplicaciones y divisiones de dos números enteros.
Los números solo se admitirán del 0 al 9.
El programa debe incluir las siguientes especificaciones:
- Una función para cada operación.
- Una función para comprobar que los números son correctos. Se admitirán números del 0 al 9. 
Introducidos como números o como cadenas (independientemente de que sean mayúsculas o minúsculas).
La función debe convertir a entero los números introducidos como cadenas.
- Una función para mostrar el menú de operaciones.
- Un algoritmo principal que realice la llamada a las funciones.
El programa debe controlar los posibles errores del usuario al introducir datos y volver a pedir los datos si es necesario.

### Ejercicio 10

Realiza un programa que tenga varias funciones para calcular el área y el perímetro de circunferencias, rectángulos, 
cuadrados y triángulos equiláteros.
El cuerpo del programa debe probar todas las funciones.

## Solucionario

1. [Intercambio de valores](ej1.py)
2. [Mayor de tres](ej2.py)
3. [Cálculo del número de Euler](ej3.py)
4. [Conteo de un caracter en una secuencia limitada](ej4.py)
5. Inversión de los dígitos de un número
   1. [Usando Strings](ej5.py)
   2. [Usando lógica matemática](ej5b.py)
6. [Números amigos](ej6.py)
7. [Número perfecto](ej7.py)
8. [Registro y login - variables globales](ej8.py)
9. [Calculadora a través de funciones](ej9.py)
10. [Áreas y perímetros](ej10.py)