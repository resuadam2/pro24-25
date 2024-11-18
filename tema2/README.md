# Tema 2 - Técnicas de diseño de programas

En este tema dejamos de programar todo en un único bloque para empezar a distribuir el código en funciones, evitando bloques de código repetitivos y empezando a refactorizar y limpiar nuestras soluciones.

También vemos como manejar la función main, muchas funciones predefinidas de Python y como importar módulos para usarlos.

Hacemos incapié en el paso de parámetros y el retorno de valores.

Para terminar con las funciones veremos también el uso de la recursividad.

Además vemos la primera estructura de datos típica de los lenguajes de programación, las listas.

Veremos también como podemos añadir complejidad a las mismas haciendo listas de listas para representar matrices.

## Apuntes y ejemplos

- [Funciones en python](./apuntes_y_ejemplos/funciones.py)
- [Alcance de las variables](./apuntes_y_ejemplos/alcance_variables.py)
- [La función main](./apuntes_y_ejemplos/funcion_main.py)
- [Listas en Python](./apuntes_y_ejemplos/listas.py)
- [Ejemplo de una posible solución del examen](./solucionario/sol_examen_ud2.py)
- [Tests unitarios para probar las funciones del examen](./solucionario/tests_examen_ud2.py)

## Enunciados ejercicios

*Nota*: Todos los ejercicios del tema anterior pueden rehacerse utilizando funciones para practicar.

### Ejercicio 1

Disear una función que intercambie el valor de dos variables de tipo entero. 
Incluir el algoritmo principal que realice la llamada a dicha función.

### Ejercicio 2

Diseñar una función que tenga como entrada tres números enteros y nos devuelva el mayor de los tres.
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

Implementar un programa de registro y login de usuarios. En primer lugar se ejecutará el código de registro, que solicitará un nombre de usuario y una  contraseña. A continuación, se ejecutará el código de login, que solicitará
el nombre de usuario y la contraseña. Si el nombre de usuario y la contraseña coinciden con los introducidos en el registro, se mostrará un mensaje de bienvenida. En caso contrario, se mostrará un mensaje de error.
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

### Ejercicio 11

Diseñar una función que determine la posición del valor máximo de una lista de enteros y otra para indicar cuál es ese valor máximo.
Incluir un programa que pruebe ambas funciones.

### Ejercicio 12

Diseñar una función que devuelva una lista invertida a partir de otra.
Incluir un programa que pruebe la función.

### Ejercicio 13

Diseñar una función para sumar dos matrices bidimensionales de enteros.
Las matrices se representarán como listas de listas y deben pasarse como argumentos a las funciones.    
Incluir un programa que pruebe ambas funciones.

### Ejercicio 14

En el ejercicio anterior ya viste que visualizar las listas como matrices simplemente imprimiendolas con print no es suficiente. Diseña una función que imprima una matriz bidimensional de enteros de manera que se vea como una matriz (no es necesario incluir los paréntesis grandes, tan solo separar los números con tabulaciones y saltos de línea). 
Incluir un programa que pruebe la función.

### Ejercicio 15

Diseñar una función para multiplicar dos matrices bidimensionales de enteros.
Las matrices se representarán como listas de listas y deben pasarse como argumentos a las funciones.
Para multiplicar dos matrices, el número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.   
La multiplicación de matrices se calcula multiplicando cada elemento de la fila de la  primera matriz por cada elemento de la columna de la segunda matriz y sumando los resultados. 
Incluir un programa que pruebe la función.

Nota: Puedes usar la función del ejercicio 14 para visualizar mejor las matrices

### Ejercicio 16

Diseñar una función que nos compruebe si una matriz bidimensional de enteros es simétrica.
Las matrices se representarán como listas de listas y deben pasarse como argumentos a las funciones.
Una matriz es simétrica si es cuadrada y es igual a su traspuesta.
La traspuesta de una matriz se obtiene intercambiando filas por columnas.
Incluir más funciones si es necesario.
Incluir un programa que pruebe la función.

### Ejercicio 17

Diseñar varias funciones para cumplir con los siguientes requisitos:
1. Función que lea una serie de números enteros positivos desde teclado y los almacene en una lista.
2. Función que reciba una lista de enteros y devuelva la suma de los elementos.
3. Función que reciba una lista de enteros y devuelva el mayor.
4. Función que reciba una lista de enteros y devuelva el menor.
5. Función que reciba una lista de enteros y devuelva la media.
6. Función que reciba una lista de enteros y devuelva la mediana.
7. Función que reciba una lista de enteros y devuelva la varianza.
8. Función que reciba una lista de enteros y devuelva la desviación típica.
9. función que reciba una lista de enteros y devuelva si es simétrica o no.
10. Función que reciba una lista de enteros y devuelva si cada elemento es un número primo o no.    
11. Función que reciba una lista de enteros y devuelva si cada elemento es un número capicúa o no.  
Incluir un programa que pruebe todas las funciones.

## Solucionario

1. [Intercambio de valores](./solucionario/ej1.py)
2. [Mayor de tres](./solucionario/ej2.py)
3. [Cálculo del número de Euler](./solucionario/ej3.py)
4. [Conteo de un caracter en una secuencia limitada](./solucionario/ej4.py)
5. Inversión de los dígitos de un número
   1. [Usando Strings](./solucionario/ej5.py)
   2. [Usando lógica matemática](./solucionario/ej5b.py)
6. [Números amigos](./solucionario/ej6.py)
7. [Número perfecto](./solucionario/ej7.py)
8. [Registro y login - variables globales](./solucionario/ej8.py)
9. [Calculadora a través de funciones](./solucionario/ej9.py)
10. [Áreas y perímetros](./solucionario/ej10.py)
11. Máximo valor de una lista
    1.  [Versión usando max()](./solucionario/ej11.py)
    2.  [Versión recorriendo la lista](./solucionario/ej11b.py)
12. Invertir una lista
    1.  [Versión con slicing](./solucionario/ej12.py)
    2.  [Versión sin slicing](./solucionario/ej12b.py)
13. [Suma de matrices](./solucionario/ej13.py)
14. [Imprimir en formato matriz](./solucionario/ej14.py)
15. [Producto de matrices](./solucionario/ej15.py)
16. [Matrices simétricas](./solucionario/ej16.py)
17. [Popurrí de funciones para trabajar con listas de enteros](./solucionario/ej17.py)

## Laboratorios del curso resueltos

- [Laboratorio ](./labs/)

### Así resolvimos los ejercicios en clase:
[Soluciones clase](./soluciones_clase/)
