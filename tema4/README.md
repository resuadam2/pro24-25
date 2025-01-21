# Tema 4 - Introducción a la Programación Orientada a Objetos (POO)

En este tema vamos a introducir la sintaxis del lenguaje Java como nuevo lenguaje de programación con el que trabajar. Una vez hecha esta introducción nos adentraremos en el mundo de la programación orientada a objetos o POO desde este lenguaje para empezar a entender sus conceptos básicos como son las clases, los objetos, los atributos y métodos de los mismos y los conceptos de Constructor, instanciación, métodos estáticos y no estáticos, los modificadores de visibilidad o acceso, etc.

## Apuntes y ejemplos

- [Apuntes tema 4 en la web](https://resuadam2-pro.vercel.app/docs/tema4/)

## Enunciados ejercicios

### Ejercicio 1

Crea una clase `Libro` que contenga los siguientes atributos: `titulo`, `autor`, `numPaginas` y `ISBN`. Crea un constructor que inicialice los atributos y métodos para obtener y modificar los mismos. Crea un método `toString` que devuelva una cadena con la información del libro.

El método `toString` debe devolver la información con el siguiente formato:

"El libro [titulo] con ISBN [ISBN] creado por el autor [autor] tiene [numPaginas] páginas."

Crea también una clase `Main` que cree un objeto de la clase `Libro`, muestre su información y modifique algunos de sus atributos.

### Ejercicio 2

Desarrollar una clase Cuenta para representar una cuenta bancaria. Los datos de la cuenta son:
nombre del cliente (String), número de cuenta (String), tipo de interés (double) y saldo (double).

La clase contendrá los siguientes métodos:

- Constructor por defecto
- Constructor con todos los parámetros
- Constructor copia (Crea un objeto Cuenta idéntico al que le llega cómo parámetro)
- Métodos setters/getters para asignar y obtener los datos de la cuenta.
- Métodos ingreso y reintegro. 
     - Un ingreso consiste en aumentar el saldo en la cantidad que se indique. Esa cantidad no puede ser negativa. 
     - Un reintegro consiste en disminuir el saldo en una cantidad pero antes se debe comprobar que hay saldo suficiente. La cantidad no puede ser negativa. 
     - Los métodos ingreso y reintegro devuelven true si la operación se ha podido realizar o false en caso contrario.
     - Método transferencia que permita pasar dinero de una cuenta a otra siempre que en la cuenta de origen haya dinero suficiente para poder hacerla.

Ejemplo de uso del método transferencia:
```java
cuentaOrigen.transferencia(cuentaDestino, importe);
```
que indica que queremos hacer una transferencia desde cuentaOrigen a cuentaDestino del importe indicado.


### Ejercicio 3

Crea una clase llamada Contador que contenga un único atributo entero llamado cont. La clase tendrá los siguientes métodos:
- **Constructor** por *defecto*
- **Constructor** con *parámetros* para inicializar el contador con un valor no negativo. Si el valor inicial quese recibe es negativo el contador tomará el valor cero como valor inicial.
- Métodos *getter* y *setter*.
- *incrementar*: incrementa el contador en una unidad.
- *decrementar*: decrementa el contador en una unidad. El contador nunca podrá tener un valornegativo. Si al decrementar se alcanza un valor negativo el contador toma el valor cero.

Una vez creada la clase, escribe un método main para probar la clase y todos sus métodos.


### Ejercicio 4

Crear una clase Java para ejecutar operaciones con fracciones de suma, resta, multiplicación y división. 

Las fracciones siempre deben estar simplificadas antes de operar con ellas, la propia clase debeencargarse de simplificarlas. 

Crear los *constructores* y métodos *getter* y *setter* necesarios, así como el método *toString*(). 

Tener en cuenta que un número no puede ser dividido entre 0.

Crear también la clase ``Main`` para poder probar todas estas operaciones.ç


### Ejercicio 5

Crea una clase Empleado que tenga los siguientes atributos privados:
Nif, Nombre, Sueldo base, Horas extra realizadas en el mes, Tipo de IRPF (%), Casado o no, Número de hijos, Importe de la hora extra (Este será estático).
Los objetos Empleado se podrán crear con un constructor vacío o con un constructor con un solo parámetro correspondiente al DNI. 
Además de los métodos getter/setter la clase Empleado tendrá estos métodos:

- Método para el cálculo del complemento correspondiente a las horas extra realizadas.
- Método para calcular el sueldo bruto (sueldo base + complemento por horas extras)
- Método para calcular las retenciones por IRPF. El porcentaje de IRPF se aplica sobre el sueldo bruto, teniendo en cuenta que el porcentaje que hay que aplicar es el tipo menos 2 puntos si el empleado está casado y menos 1 punto adicional por cada hijo que tenga.
- Método *toString*() para mostrar los datos de los empleados de la siguiente forma:
```plaintext
12345678A Lucas Guerrero Arjona
Sueldo Base: 1150.0
Horas Extras: 4
tipo IRPF: 15.0
Casado: S
Número de Hijos: 2
```
Una vez creada la clase Empleado, crearemos una clase Main y la utilizaremos para que lea empleados y los guarde en un array estático.
El número total de empleados se pide por teclado. El número máximo de empleados es de 20.
Después de leer los datos de los empleados se pedirá que se introduzca el importe correspondiente al pago por hora extra asignándoselo al atributo estático de la clase.
A continuación el programa mostrará:
     1. El empleado que más cobra y el que menos
     2. El empleado que cobra más por horas extra y el que menos.
     3. Todos los empleados ordenados por salario de menor a mayor.

### Ejercicio 6

Crear una clase NIF que represente el DNI con su correspondiente letra. Los atributos de la clase serán el número de DNI y su letra. 

La clase NIF dispondrá de los siguientes métodos:
- Un constructor vacío.
- Un constructor que reciba como parámetro el DNI y calcule y asigne la letra que le corresponde.
- Un método leer(): que pida por teclado el número de DNI y calcule a partir del DNI introducido la letra que le corresponde.
- Método toString() que muestre el NIF de la siguiente forma: ocho dígitos, un guión y la letra en mayúscula. Por ejemplo: 12345678-Z.

- Método para obtener la letra del NIF:
La letra del NIF se calculará usando un método privado. La forma de obtener la letra del NIF es la siguiente:
Se obtiene el resto de la división entera del número de DNI entre 23 y se usa la siguiente tabla para obtener la letra que corresponde:

0 - T 1 - R 2 - W 3 - A 4 - G 5 – M

6 – Y 7 – F 8 – P 9 - D 10 – X 11 – B

12 – N 13 – J 14 – Z 15 – S 16 - Q 17 - V

18 - H 19 - L 20 – C 21 – K 22 – E

Una vez creada la clase, escribe una clase principal para probarla.


### Ejercicio 7

Crear una Clase Fecha en Java. La clase tendrá tres atributos privados dia, mes y año de tipo entero. La clase contendrá los siguientes métodos:
- *Constructor* vacío.
- *Constructor* con tres parámetros para crear objetos con valores iniciales.
- Métodos *set* y *get* para asignar y obtener los valores de los atributos de la clase.
- Método *fechaCorrecta*() que comprueba si la fecha es correcta. Devuelve un valor de tipo boolean indicando si la fecha es correcta o no. 
Este método a su vez utilizará un método privado de la clase llamado esBisiesto() que calcula si el año es o no bisiesto. El método esBisiesto devuelve true si el año es bisiesto y false si no lo es.
- Método *diaSiguiente*() que cambia la fecha actual por la del día siguiente. 
El objeto de la clase Fecha al que se le aplique este método deberá quedar siempre en un estado consistente, es decir, la nueva fecha deberá ser correcta.
- Modificar el método *toString*() para mostrar las fechas de la forma dd-mm-aaaa. El día y el mes se deben mostrar con dos cifras. 
Si el dia o el mes tienen solo una cifra se escribirá un cero delante. Por ejemplo si la fecha es dia=1, mes=6, año= 2015 la fecha que se mostrará será: 01-06-2015.

Escribe un programa para probar la clase Fecha. 
El método *diaSiguiete*() se debe probar dentro de un bucle que imprima la fecha durante cada iteración del bucle, hasta un punto.


### Ejercicio 8

Crea una clase ``Persona`` con los siguientes atributos: ``nombre``, ``dirección``, ``codigoPostal``, ``ciudad`` y ``fechaNacimiento``. 
El atributo ``fechaNacimiento`` es un objeto de la clase ``Fecha`` creada el ejercicio anterior. Las clases ``Persona`` y ``Fecha`` tienen por tanto una relación de composición.

A la clase ``Fecha`` que ya tenemos le añadiremos un método boolean *esMayorQue(Fecha f)*  . Este método devuelve ``true`` si la fecha que contiene el objeto es mayor que la fecha que recibe como parámetro y ``false`` en caso contrario.
La clase Persona contendrá los siguientes métodos:
- *Constructor*
- Métodos *get* y *set*
- Método boolean *esMayorDeEdad*() que devuelve true si la persona es mayor de edad y false en caso contrario. Para saber si la persona es mayor de edad se comparará la fecha de nacimiento con la fecha actual obtenida del sistema.
- Método *toString*() que muestre los datos de la siguiente forma:
```plaintext
Nombre: Juan José Pérez Gómez
Fecha Nacimiento: 23-09-1967
Dirección: C/ Pizarro 32 5oA
36204 Vigo
```

La clase ``Persona`` será utilizada en un main que pida por teclado los datos de varias personas y las guarde en un **ArrayList** de objetos de tipo ``Persona`` y a continuación muestre información sobre ellas.

A continuación del método main se escribirá el código del resto de métodos de la clase principal.

- Método *leerPersonas*(): pide por teclado los datos de las personas y las añade al array.
- Método *mostrar*(): muestra los datos de todas las personas introducidas.
- Método *numeroDePersonas*(): devuelve el número de personas que contiene el array.
- Método *personaMayorEdad*(): devuelve la persona de mayor edad. Si hay varias devuelve la primera encontrada.
- Método *cuantasPersonasVivenEn(String)* : método que recibe el nombre de una población y devuelve cuántas de esas personas viven en ella.
- Método *personasMayoresDeEdad*(): método que devuelve cuántas de esas personas son mayores de edad.


### Ejercicio 9

Crear un programa sobre una **sala de cine** que tiene un ``conjunto de asientos`` (8 filas por 9 columnas, por ejemplo). 

Del **cine** interesa conocer la ``película`` que se está reproduciendo y el ``precio`` de la entrada en el cine. 

De las **películas** interesa saber el ``título``, ``duración``, ``edad mínima`` y ``director``. Del **espectador** interesa saber su ``nombre``, ``edad`` y el ``dinero`` que tiene. 

Los **asientos** son etiquetados por una ``letra`` (columna) y un ``número`` (fila), la fila 1 empieza al final de la matriz como se muestra en la tabla.  También deberemos saber si está ``ocupado`` o no el asiento.

```plaintext
8 A 8 B 8 C 8 D 8 E 8 F 8 G 8 H 8 I
7 A 7 B 7 C 7 D 7 E 7 F 7 G 7 H 7 I
6 A 6 B 6 C 6 D 6 E 6 F 6 G 6 H 6 I
5 A 5 B 5 C 5 D 5 E 5 F 5 G 5 H 5 I
4 A 4 B 4 C 4 D 4 E 4 F 4 G 4 H 4 I
3 A 3 B 3 C 3 D 3 E 3 F 3 G 3 H 3 I
2 A 2 B 2 C 2 D 2 E 2 F 2 G 2 H 2 I
1 A 1 B 1 C 1 D 1 E 1 F 1 G 1 H 1 I
```

Se realizará una pequeña simulación, en la que se generarán muchos espectadores y se sentarán aleatoriamente (no se puede ver donde ya esté ocupado). 
Los espectadores se sentarán de uno en uno. 
Solo se podrá sentar si tienen el suficiente dinero, hay espacio libre y tiene edad para ver la película, en caso de que el asiento esté ocupado se le buscará uno libre. 
Los datos del espectador y la película pueden ser totalmente aleatorios.


## [Solucionario](./solucionario/)

### Así resolvimos los ejercicios en clase:
[Soluciones clase](./soluciones_clase/)
