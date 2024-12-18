/**
 * Vamos a hablar sobre métodos en Java.
 *
 * Un método es un bloque de código que se ejecuta cuando se le llama.
 *
 * Puedes pasar datos, conocidos como parámetros, a un método.
 */
public class Main {
    /**
     * Sobre la palabra reservada static:
     * En Java, los métodos se definen como static o no static.
     * Los métodos static se pueden llamar sin crear un objeto de la clase.
     * Los métodos static se llaman a través de la clase, no a través de un objeto.
     * Podríamos decir que son métodos de clase.
     * Cuando veamos más en detalle la programación orientada a objetos, veremos que los métodos no static se llaman métodos de instancia.
     */
    public static void main(String[] args) {
        // Llamamos al método myMethod
        myMethod();

        // Llamamos al método myMethodWithParameter
        myMethodWithParameter("John");

        // Llamamos al método myMethodWithTwoParameters
        myMethodWithTwoParameters("John", 30);

        // Llamamos al método myMethodWithReturnValue
        int result = myMethodWithReturnValue(5, 3);
        System.out.println("The result is: " + result);

        // Llamamos al método myMethodWithVariableParameters
        int result2 = myMethodWithVariableParameters(1, 2, 3, 4, 5);
        System.out.println("The result is: " + result2);
    }

    /**
     * En Java, los métodos se definen dentro de una clase.
     *
     * Los métodos deben definir un modificador de acceso, seguido de un tipo de retorno, seguido de un nombre, seguido de paréntesis ().
     * El cuerpo del método se define entre llaves {}.
     *
     * Los métodos definen el tipo de retorno, que es el tipo de dato que el método devolverá después de su
     * ejecución. Si un método no devuelve un valor, el tipo de retorno es void.
     *
     * Los métodos pueden tener parámetros, que son valores que se pasan al método.
     * El tipo de dato y el nombre de los parámetros se definen en el método.
     * Al ser Java un lenguaje fuertemente tipado, los parámetros deben ser del tipo de dato definido en el método.
     * Si al pasar los parámetros al método, no se pasan en el orden correcto, se producirá un error de compilación.
     *
     */

    // Creamos un método llamado myMethod
    private static void myMethod() {
        System.out.println("I just got executed!");
    }

    // Esto es un método que recibe un parámetro
    private static void myMethodWithParameter(String name) {
        System.out.println("Hello " + name);
    }

    // Esto es un método que recibe dos parámetros
    private static void myMethodWithTwoParameters(String name, int age) {
        System.out.println("Hello " + name + ", you are " + age + " years old");
    }

    // Esto es un método que retorna un valor
    private static int myMethodWithReturnValue(int x, int y) {
        return x + y;
    }

    // Esto es un método que recibe un número variable de parámetros
    private static int myMethodWithVariableParameters(int... numbers) {
        int result = 0;
        for (int i : numbers) {
            result += i;
        }
        return result;
    }

    /**
     * En java, los métodos pueden ser de varios tipos:
     *
     * 1. Métodos sin retorno y sin parámetros
     * 2. Métodos sin retorno y con parámetros
     * 3. Métodos con retorno y sin parámetros
     * 4. Métodos con retorno y con parámetros
     * 5. Métodos con retorno y con un número variable de parámetros
     * 6. Métodos sin retorno y con un número variable de parámetros
     */
}