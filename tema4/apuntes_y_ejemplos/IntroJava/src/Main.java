/**
 * En Java podemos hacer comentarios de una sola línea con // y comentarios de varias líneas con /* y * /.
 */

/**
 * Introducción a la sintaxis de Java
 *
 * En este archivo se muestra la estructura básica de un archivo en Java.
 * Todo archivo en Java debe tener una clase con el mismo nombre que el archivo.
 *
 * En este caso, el archivo se llama Main.java y la clase se llama Main.
 *
 * Podemos compilar y ejecutar los archivos Java por línea de comandos.
 *
 * Para compilar:
 * javac Main.java
 *
 * Para ejecutar:
 * java Main
 */
public class Main {
    /**
     * Método principal de la clase Main
     * @param args Argumentos que se pasan al ejecutar el programa
     * por línea de comandos:
     *             java Main
     *             java Main arg1 arg2 arg3
     *
     * El método main es el punto de entrada de un programa en Java.
     *
     * Es el método que se ejecuta cuando se ejecuta el programa y por lo tanto
     *  es el punto de inicio de la ejecución del programa.
     */
    public static void main(String[] args) {
        // Empecemos por lo más básico, imprimir un mensaje en la consola
        System.out.println("Hola Mundo!");

        /**
         * System es una clase que contiene varios métodos y propiedades útiles.
         * out es una propiedad de la clase System que representa la salida estándar.
         * println es un método de la clase PrintStream que imprime una línea de texto.
         */

        // Podemos imprimir variables
        int numero = 10; // Declaración de una variable de tipo entero
        System.out.println(numero); // Imprime el valor de la variable numero

        double decimal = 3.14; // Declaración de una variable de tipo double
        System.out.println(decimal); // Imprime el valor de la variable decimal

        boolean booleano = true; // Declaración de una variable de tipo boolean
        System.out.println(booleano); // Imprime el valor de la variable booleano

        char caracter = 'a'; // Declaración de una variable de tipo char
        System.out.println(caracter); // Imprime el valor de la variable caracter

        String cadena = "Hola Mundo!"; // Declaración de una variable de tipo String
        System.out.println(cadena); // Imprime el valor de la variable cadena

        float flotante = 3.14f; // Declaración de una variable de tipo float
        System.out.println(flotante); // Imprime el valor de la variable flotante

        long largo = 1000000000L; // Declaración de una variable de tipo long
        System.out.println(largo); // Imprime el valor de la variable largo

        short corto = 100; // Declaración de una variable de tipo short
        System.out.println(corto); // Imprime el valor de la variable corto

        byte byte1 = 100; // Declaración de una variable de tipo byte
        System.out.println(byte1); // Imprime el valor de la variable byte1

        /**
         * Hablemos sobre el tipado y los tipos de datos en Java.
         * Java es un lenguaje de programación fuertemente tipado.
         * Esto quiere decir que las variables deben ser declaradadas con un tipo de dato específico.
         * Java tiene varios tipos de datos primitivos:
         *
         * - byte: 8 bits, valores entre -128 y 127
         * - short: 16 bits, valores entre -32,768 y 32,767
         * - int: 32 bits, valores entre -2,147,483,648 y 2,147,483,647
         * - long: 64 bits, valores entre -9,223,372,036,854,775,808 y 9,223,372,036,854,775,807
         * - float: 32 bits, valores entre 1.4e-45 y 3.4e+38
         * - double: 64 bits, valores entre 4.9e-324 y 1.8e+308
         * - char: 16 bits, valores entre '\u0000' y '\uffff'
         * - boolean: valores true o false
         *
         * Además de los tipos de datos primitivos, Java también tiene tipos de datos no primitivos.
         * Estos son objetos que se crean a partir de clases.
         *
         * - String: secuencia de caracteres
         * - Arrays: colección de elementos del mismo tipo
         * - Classes: plantillas para crear objetos
         * - Interfaces: colección de métodos abstractos
         * - Enums: enumeraciones
         * - Null: indica que una variable no tiene valor
         *
         * En Java, las variables deben ser declaradas antes de ser utilizadas.
         * La declaración de una variable se hace de la siguiente forma:
         *
         * tipo nombreVariable;
         *
         * Por ejemplo:
         *
         * int numero;
         *
         * Para asignar un valor a una variable, se utiliza el operador de asignación (=).
         *
         * nombreVariable = valor;
         *
         * Por ejemplo:
         *
         * numero = 10;
         *
         * También se puede declarar y asignar un valor a una variable en la misma línea.
         *
         * tipo nombreVariable = valor;
         *
         * Por ejemplo:
         *
         * int numero = 10;
         *
         * Las variables en Java son sensibles a mayúsculas y minúsculas.
         * Esto quiere decir que el nombre de una variable puede contener letras mayúsculas y minúsculas.
         *
         * Java es un lenguaje de tipado estático.
         * Esto quiere decir que el tipo de una variable no puede cambiar una vez que ha sido declarada.
         * Sin embargo, el valor de una variable puede cambiar durante la ejecución del programa.
         * Más adelante veremos como castear variables para cambiar su tipo a la hora de asignar un valor.
         */

        // Podemos hacer operaciones matemáticas
        int suma = 10 + 5; // Suma
        System.out.println(suma); // Imprime el resultado de la suma

        int resta = 10 - 5; // Resta
        System.out.println(resta); // Imprime el resultado de la resta

        int multiplicacion = 10 * 5; // Multiplicación
        System.out.println(multiplicacion); // Imprime el resultado de la multiplicación

        int division = 10 / 5; // División
        System.out.println(division); // Imprime el resultado de la división

        int modulo = 10 % 3; // Módulo
        System.out.println(modulo); // Imprime el resultado del módulo

        // Podemos hacer operaciones lógicas
        boolean igual = 10 == 10; // Igualdad
        System.out.println(igual); // Imprime el resultado de la igualdad

        boolean diferente = 10 != 10; // Diferencia
        System.out.println(diferente); // Imprime el resultado de la diferencia

        boolean mayor = 10 > 5; // Mayor que
        System.out.println(mayor); // Imprime el resultado de mayor que

        boolean menor = 10 < 5; // Menor que
        System.out.println(menor); // Imprime el resultado de menor que

        boolean mayorIgual = 10 >= 10; // Mayor o igual que
        System.out.println(mayorIgual); // Imprime el resultado de mayor o igual que

        boolean menorIgual = 10 <= 5; // Menor o igual que
        System.out.println(menorIgual); // Imprime el resultado de menor o igual que

        // Podemos hacer operaciones lógicas con booleanos
        boolean and = true && false; // AND
        System.out.println(and); // Imprime el resultado de la operación AND

        boolean or = true || false; // OR
        System.out.println(or); // Imprime el resultado de la operación OR

        boolean not = !true; // NOT
        System.out.println(not); // Imprime el resultado de la operación NOT

        // Podemos hacer operaciones con cadenas
        String cadena1 = "Hola";
        String cadena2 = " Mundo!";
        String concatenacion = cadena1 + cadena2; // Concatenación
        System.out.println(concatenacion); // Imprime el resultado de la concatenación

        // Podemos hacer operaciones con caracteres
        char caracter1 = 'a';
        char caracter2 = 'b';
        int sumaCaracteres = caracter1 + caracter2; // Suma de caracteres
        System.out.println(sumaCaracteres); // Imprime el resultado de la suma de caracteres

        // Podemos hacer operaciones con números decimales
        double numero1 = 3.14;
        double numero2 = 2.71;
        double sumaDecimales = numero1 + numero2; // Suma de decimales
        System.out.println(sumaDecimales); // Imprime el resultado de la suma de decimales

        // Podemos hacer operaciones con números enteros y decimales
        int entero = 10;
        double decimal1 = 3.14;
        double sumaEnteroDecimal = entero + decimal1; // Suma de entero y decimal
        System.out.println(sumaEnteroDecimal); // Imprime el resultado de la suma de entero y decimal

        /**
         * En Java, los operadores se utilizan para realizar operaciones sobre variables y valores.
         *
         * Los operadores aritméticos se utilizan para realizar operaciones matemáticas:
         *
         * - Suma (+): suma dos valores
         * - Resta (-): resta dos valores
         * - Multiplicación (*): multiplica dos valores
         * - División (/): divide dos valores
         * - Módulo (%): devuelve el resto de la división de dos valores
         *
         * Los operadores de comparación se utilizan para comparar dos valores:
         *
         * - Igualdad (==): devuelve true si dos valores son iguales
         * - Diferencia (!=): devuelve true si dos valores son diferentes
         * - Mayor que (>): devuelve true si el primer valor es mayor que el segundo
         * - Menor que (<): devuelve true si el primer valor es menor que el segundo
         * - Mayor o igual que (>=): devuelve true si el primer valor es mayor o igual que el segundo
         * - Menor o igual que (<=): devuelve true si el primer valor es menor o igual que el segundo
         *
         * Los operadores lógicos se utilizan para combinar expresiones lógicas:
         *
         * - AND (&&): devuelve true si ambas expresiones son verdaderas
         * - OR (||): devuelve true si al menos una de las expresiones es verdadera
         * - NOT (!): devuelve true si la expresión es falsa
         *
         * Los operadores de asignación se utilizan para asignar un valor a una variable:
         *
         * - Asignación (=): asigna un valor a una variable
         * - Suma y asignación (+=): suma un valor a una variable y asigna el resultado a la variable
         * - Resta y asignación (-=): resta un valor a una variable y asigna el resultado a la variable
         * - Multiplicación y asignación (*=): multiplica un valor a una variable y asigna el resultado a la variable
         * - División y asignación (/=): divide un valor a una variable y asigna el resultado a la variable
         * - Módulo y asignación (%=): calcula el módulo de un valor a una variable y asigna el resultado a la variable
         *
         * Los operadores de concatenación se utilizan para concatenar cadenas:
         *
         * - Concatenación (+): concatena dos cadenas
         *
         * Los operadores de incremento y decremento se utilizan para incrementar o decrementar una variable en una unidad:
         *
         * - Incremento (++): incrementa una variable en una unidad
         * - Decremento (--): decrementa una variable en una unidad
         *
         */
    }
}