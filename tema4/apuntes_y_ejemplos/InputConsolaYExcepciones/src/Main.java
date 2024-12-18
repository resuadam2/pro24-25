import java.util.InputMismatchException;
import java.util.Scanner;

/**
 * Vamos a ver como leer la entrada de datos por consola en Java.
 * Además de esto, aprovecharemos para ver como funciona la captura de excepciones.
 */
public class Main {
    /**
     * Para leer la entrada de datos en Java tenemos varias opciones:
     * - BufferedReader (para grandes volúmenes de datos)
     * - Scanner (para tipos primitivos y cadenas)
     * - DataInputStream (no recomendado)
     * - Console (no funciona en algunos IDEs)
     *
     * En este caso vamos a utilizar la clase Scanner.
     * Para ello, primero debemos importar la clase java.util.Scanner.
     *
     */

    public static void main(String[] args) {
//        int numero = leerEntero();
//        System.out.println("Número introducido: " + numero);
        // Para ejecutar leerDatos, comentar la llamada a leerEntero, si no saltará una excepción.
        // leerDatos();
        // Para ejecutar leerDatosCorregido, comentar la llamada a leerDatos, si no saltará una excepción.
        leerDatosCorregido();

        try {
            int resultado = dividir(10, 2);
            System.out.println("Resultado: " + resultado);
        } catch (ArithmeticException e) {
            System.out.println("Error: " + e.getMessage());
        }

        try {
            int resultado = dividir(10, 0);
            System.out.println("Resultado: " + resultado);
        } catch (ArithmeticException e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            System.out.println("Fin del programa.");
        }
    }

    /**
     * Método que lee un número entero por consola.
     * @return Número entero introducido por el usuario.
     */
    private static int leerEntero() {
        int numero = 0;
        boolean error = true;
        do {
            try {
                System.out.print("Introduce un número entero: ");
                Scanner sc = new Scanner(System.in); // Inicializamos el objeto Scanner.
                numero = sc.nextInt(); // Leemos un número entero, si no es un número entero, se lanza una excepción.
                error = false;
                sc.close(); // Cerramos el flujo de entrada.
            } catch (InputMismatchException e) {
                System.out.println("Error: No has introducido un número entero.");
            }
        } while (error); // Repetimos el bucle mientras haya error.

        return numero; // Devolvemos el número introducido por el usuario.
    }

    /**
     * Como podemos observar, la clase Scanner nos proporciona métodos para leer datos de diferentes tipos.
     *
     * - nextInt(): Lee un número entero.
     * - nextDouble(): Lee un número decimal.
     * - next(): Lee una cadena de texto.
     * - nextLine(): Lee una línea de texto.
     * - nextBoolean(): Lee un valor booleano.
     * - nextByte(): Lee un número byte.
     * - nextShort(): Lee un número short.
     * - nextLong(): Lee un número long.
     * - nextFloat(): Lee un número float.
     * - nextBigInteger(): Lee un número BigInteger.
     * - nextBigDecimal(): Lee un número BigDecimal.
     *
     * Además de esto, la clase Scanner nos proporciona métodos para comprobar si hay más datos por leer.
     *
     * - hasNext(): Devuelve true si hay más datos por leer.
     * - hasNextInt(): Devuelve true si hay más números enteros por leer.
     * - hasNextDouble(): Devuelve true si hay más números decimales por leer.
     * - hasNextLine(): Devuelve true si hay más líneas de texto por leer.
     * - hasNextBoolean(): Devuelve true si hay más valores booleanos por leer.
     * - hasNextByte(): Devuelve true si hay más números byte por leer.
     * - hasNextShort(): Devuelve true si hay más números short por leer.
     * - hasNextLong(): Devuelve true si hay más números long por leer.
     * - hasNextFloat(): Devuelve true si hay más números float por leer.
     * - hasNextBigInteger(): Devuelve true si hay más números BigInteger por leer.
     * - hasNextBigDecimal(): Devuelve true si hay más números BigDecimal por leer.
     *
     * Por último, la clase Scanner nos proporciona métodos para cerrar el flujo de entrada.
     *
     * - close(): Cierra el flujo de entrada.
     *
     * Es importante cerrar el flujo de entrada una vez que hayamos terminado de leer datos.
     * De esta forma, liberamos recursos y evitamos posibles problemas de memoria.
     *
     * En el caso de que no cerremos el flujo de entrada, podemos tener problemas de memoria.
     *
     */

    private static void leerDatos() {
        /**
         * Vamos a ver un problema al usar Scanner con next() y nextLine().
         * Cuando leemos una cadena de texto con next(), no se lee el salto de línea.
         * Por lo tanto, si después leemos una línea de texto con nextLine(), se salta la lectura.
         * Esto ocurre también al leer un número entero con nextInt() y después leer una línea de texto con nextLine().
         */
        Scanner sc = new Scanner(System.in);
        System.out.print("Introduce tu nombre: ");
        String nombre = sc.next();
        System.out.print("Introduce tu edad: ");
        int edad = sc.nextInt();
        System.out.print("Introduce tu ciudad: ");
        String ciudad = sc.nextLine();
        System.out.println("Nombre: " + nombre);
        System.out.println("Edad: " + edad);
        System.out.println("Ciudad: " + ciudad);
        sc.close();
    }

    /**
     * Para solucionar este problema, podemos usar el método nextLine() después de leer un número entero.
     * De esta forma, leemos el salto de línea y evitamos que se salte la lectura.
     * También podemos usar el método nextLine() después de leer una cadena de texto.
     * De esta forma, leemos el salto de línea y evitamos que se salte la lectura.
     * Además de esto, podemos usar el método nextLine() después de leer un número entero con nextInt().
     * De esta forma, leemos el salto de línea y evitamos que se salte la lectura.
     * También podemos usar el método nextLine() después de leer una cadena de texto con next().
     * De esta forma, leemos el salto de línea y evitamos que se salte la lectura.
     */

    private static void leerDatosCorregido() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Introduce tu nombre: ");
        String nombre = sc.next();
        System.out.print("Introduce tu edad: ");
        int edad = sc.nextInt();
        sc.nextLine(); // Leemos el salto de línea.
        System.out.print("Introduce tu ciudad: ");
        String ciudad = sc.nextLine();
        System.out.println("Nombre: " + nombre);
        System.out.println("Edad: " + edad);
        System.out.println("Ciudad: " + ciudad);
        sc.close();

        /**
         * En este caso, hemos usado el método nextLine() después de leer un número entero con nextInt().
         * De esta forma, leemos el salto de línea y evitamos que se salte la lectura.
         * También hemos usado el método nextLine() después de leer una cadena de texto con next().
         * De esta forma, leemos el salto de línea y evitamos que se salte la lectura.
         */

    }

    /**
     * Sobre el control de excepciones, podemos ver que hemos usado un bloque try-catch.
     * En este caso, hemos capturado la excepción InputMismatchException.
     * Esta excepción se lanza cuando el usuario introduce un valor que no es un número entero.
     * Por lo tanto, hemos capturado esta excepción para mostrar un mensaje de error.
     * Hemos usado un bucle do-while para repetir la lectura mientras haya error.
     * Así obligamos al usuario a introducir un número entero válido.
     *
     * La sintaxis para la captura de excepciones es la siguiente:
     *
     * try {
     *    // Código que puede lanzar una excepción.
     *    // Si se lanza una excepción, se salta al bloque catch.
     *    // Si no se lanza una excepción, se ejecuta el código normalmente.
     *
     * } catch (Excepción e) {
     *   // Código que se ejecuta si se lanza una excepción.
     * } finally {
     *  // Código que se ejecuta siempre, tanto si se lanza una excepción como si no.
     *  }
     *
     *  En este caso, hemos usado un bloque try-catch para capturar la excepción InputMismatchException.
     *
     *  Otras excepciones que podemos capturar son:
     *  - ArithmeticException: Se lanza cuando se produce un error aritmético.
     *  - ArrayIndexOutOfBoundsException: Se lanza cuando se intenta acceder a un índice fuera de los límites de un array.
     *  - ClassNotFoundException: Se lanza cuando no se encuentra una clase.
     *  - IOException: Se lanza cuando se produce un error de entrada/salida.
     *  - SQLException: Se lanza cuando se produce un error de base de datos.
     *  - NullPointerException: Se lanza cuando se intenta acceder a un objeto nulo.
     *  - NumberFormatException: Se lanza cuando se produce un error al convertir una cadena de texto a un número.
     *  - FileNotFoundException: Se lanza cuando no se encuentra un archivo.
     *  - InterruptedException: Se lanza cuando se interrumpe un hilo.
     *  - OutOfMemoryError: Se lanza cuando no hay suficiente memoria disponible.
     *  - StackOverflowError: Se lanza cuando se desborda la pila de llamadas.
     *  - IllegalArgumentException: Se lanza cuando se pasa un argumento no válido a un método.
     *  - IllegalStateException: Se lanza cuando se produce un estado no válido.
     *  - UnsupportedOperationException: Se lanza cuando se intenta realizar una operación no soportada.
     *
     *  Existen muchas más excepciones en Java, pero estas son las más comunes.
     *  Para conocer todas las excepciones de Java, podemos consultar la documentación oficial.
     *
     *  También podemos capturar excepciones genéricas:
     *  - Exception: Captura cualquier excepción.
     *  - Throwable: Captura cualquier error o excepción.
     *  - Error: Captura cualquier error.
     *  - RuntimeException: Captura cualquier excepción en tiempo de ejecución.
     *
     *  Las excepciones se pueden lanzar con la instrucción throw.
     *  Por ejemplo, podemos lanzar una excepción si el usuario introduce un número negativo.
     *
     *  Vamos a ver un ejemplo de esto.
     */

    private static int dividir(int a, int b) throws ArithmeticException {
        if (b == 0) {
            throw new ArithmeticException("No se puede dividir por cero.");
        }
        return a / b;
    }

    /**
     * Las palabras reservadas throw y throws se utilizan para lanzar excepciones.
     * La palabra reservada throw se utiliza para lanzar una excepción en un método.
     * La palabra reservada throws se utiliza para declarar que un método puede lanzar una excepción.
     * En este caso, hemos declarado que el método dividir puede lanzar una excepción ArithmeticException.
     * Por lo tanto, si se produce un error al dividir por cero, se lanzará una excepción.
     * Throws nos sirve para informar al programador que un método puede lanzar una excepción y
     * por lo tanto, debe ser capturada o propagarla.
     *
     * También podemos lanzar excepciones personalizadas.
     * Para ello, debemos crear una clase que herede de Exception o RuntimeException.
     * Pero esto lo veremos más adelante, cuando veamos herencia y polimorfismo.
     */

}