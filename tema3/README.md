# Tema 3 - Tipos de datos estructurados

En este tema vemos antes de nada la captura de excepciones en bloques try-except, junto con sus variantes con else y finally.

También vemos otras 3 nuevas estructuras de datos básicas de Python pero existentes en muchos otros lenguajes como son las tuplas, los diccionarios y los conjuntos.

## Apuntes y ejemplos

- [Captura de excepciones en Python (bloques try-except y derivados)](./apuntes_y_ejemplos/try_except.py)
- [Tuplas en Python](./apuntes_y_ejemplos/tuplas.py)
- [Diccionarios en Python](./apuntes_y_ejemplos/diccionarios.py)
- [Conjuntos en Python](./apuntes_y_ejemplos/conjuntos.py)
- [Ejemplo usos de random en Python](./apuntes_y_ejemplos/uso_random.py)
- [Ejemplo de una posible solución del examen](./solucionario/sol_examen_ud3.py)


## Enunciados ejercicios

*Nota*: En todos los ejercicios debe hacerse una captura de las posibles excepciones.

### Ejercicios de control de excepciones

1. Escribir una función que reciba dos números y devuelva su división. Si el segundo número es cero debe devolver un mensaje de error.
2. Escribir una función que reciba una lista de números y devuelva su media. Si la lista está vacía debe devolver un mensaje de error.
3. Escribir una función que reciba una cadena y un número n y devuelva la cadena repetida n veces. Si el número es negativo debe devolver un mensaje de error. 
4. Escribir una función que reciba una lista de números y devuelva una lista con los cuadrados de los números. Si la lista contiene algún elemento que no es un número debe devolver un mensaje de error.    
5. Escribir una función que reciba una tupla y una posición y devuelva el elemento de la tupla en la posición indicada. Si la posición es mayor que la longitud de la tupla debe devolver un mensaje de error.
6. Escribir una función que reciba un diccionario y una clave y devuelva el valor asociado a la clave. Si la clave no existe debe devolver un mensaje de error.  
7. Escribir una función que reciba una lista de números y devuelva el número más grande. Si la lista está vacía debe devolver un mensaje de error.   

### Ejercicios de uso de Conjuntos (set)

1. Escribir una función que reciba dos conjuntos y devuelva un conjunto con los elementos que están en ambos conjuntos.
2. Escribir una función que reciba dos conjuntos y devuelva un conjunto con los elementos que están en el primer conjunto pero no en el segundo. 
3. Escribir una función que reciba dos conjuntos y devuelva un conjunto con los elementos que están en alguno de los dos conjuntos pero no en los dos. 
4. Escribir una función que reciba una lista de enteros y devuelva otra lista sin elementos repetidos, para ello se puede convertir la lista en un conjunto y después volver a convertirlo en lista. 
5. Escribir una función que reciba una lista de palabras y devuelva un conjunto con las palabras que tienen más de n caracteres. 
6. Escribir una función que dadas dos palabras devuelva un conjunto con las letras que tienen en común.
7. Escribir una función que reciba dos listas y nos diga si la primera lista está contenida en la segunda o no, utiliza operadores de conjuntos para ello.

### Ejercicios de uso de Tuplas

1. Escribir una función que reciba una tupla de elementos e indique si se encuentran ordenados de menor a mayor o no. 
2. Escribir una función que reciba una tupla de elementos e indique si se encuentran ordenados de mayor a menor o no.
3. Escribir una función que reciba una tupla de elementos e indique si son todos distintos o no. 
4. Escribir una función que reciba una tupla de elementos e indique si es capicúa o no. 
5. Escribir una función que reciba una tupla de números y un valor n y devuelva una lista con los elementos de la tupla que son múltiplos de n.
6. Escribir una función que reciba una tupla de números y devuelva su máximo y su mínimo.  
7. Escribir una función que reciba una tupla de números y devuelva su media y su varianza. 
8. Escribir una función que reciba una tupla de números y devuelva la tupla con sus elementos ordenados de menor a mayor.
  
### Ejercicios de uso de Diccionarios

1. Escribir una función que reciba un diccionario con las asignaturas y las notas de un alumno y devuelva otro diccionario con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas aprobadas.    
2. Escribir una función que reciba un diccionario con el horario de un alumno y lo recorra imprimiendo los días de la semana y las asignaturas que tiene en cada uno.
3. Escribir una función que reciba un diccionario con los precios de distintos productos y un diccionario con los productos y la cantidad de cada uno que ha comprado un cliente y devuelva el precio total de la compra.
4. Escribir una función que reciba un diccionario con las asignaturas y las notas de un alumno y devuelva la media de las notas. 
5. Escribir una función que reciba un diccionario con los planetas del sistema solar y sus distancias al sol, además debe recibir un planeta y devolver su distancia a la Tierra. Las distancias se expresan en millones de kilómetros. La distancia de la Tierra al Sol es de 149.6 millones de kilómetros. La distancia de los planetas al Sol son las siguientes:
   - Mercurio: 57.9
   - Venus: 108.2
   - Tierra: 149.6
   - Marte: 227.9
   - Júpiter: 778.5
   - Saturno: 1433.4
   - Urano: 2872.5
   - Neptuno: 4495.1
   - Plutón: 5906.4
6. Escribir una función que reciba una lista de palabras y devuelva un diccionario con las palabras como claves y su longitud como valor.
7. Escribir una función que reciba una lista de palabras y devuelva un diccionario con las palabras como claves y el número de veces que aparecen como valor.

## Solucionario

1. [Ejercicios control de excepciones](./solucionario/ejersExcepciones.py)
2. [Ejercicios con Conjuntos](./solucionario/ejersConjuntos.py)
3. [Ejercicios con Tuplas](./solucionario/ejersTuplas.py)
4. [Ejercicios con Diccionarios](./solucionario/ejersDiccionarios.py)

### Así resolvimos los ejercicios en clase:
[Soluciones clase](./soluciones_clase/)
