// Importamos la clase Arrays del paquete java.util para acceder a los métodos de la clase Arrays.
import java.util.Arrays;

/**
 * Vamos a hablar sobre los arrays en Java.
 * Un array es un conjunto de elementos del mismo tipo.
 * En java, los arrays son objetos, por lo que se pueden aplicar métodos sobre ellos.
 * A diferencia de otras estructuras de datos vistas en Python, los arrays en Java tienen un tamaño fijo.
 */


public class Main {
    public static void main(String[] args) {
        // Declaración de un array de enteros
        int[] numeros = new int[5];
        // Inicialización de un array de enteros
        int[] numeros2 = {1, 2, 3, 4, 5};
        // Declaración e inicialización de un array de enteros
        int[] numeros3 = new int[]{1, 2, 3, 4, 5};

        // Acceso a un elemento de un array
        System.out.println(numeros2[0]); // 1
        // Modificación de un elemento de un array
        numeros2[0] = 10;
        System.out.println(numeros2[0]); // 10

        // Iteración sobre un array
        for (int i = 0; i < numeros2.length; i++) {
            System.out.println(numeros2[i]);
        }

        // Iteración sobre un array con un bucle for-each
        for (int numero : numeros2) {
            System.out.println(numero);
        }

        // Arrays multidimensionales
        int[][] matriz = new int[2][3];
        int[][] matriz2 = {{1, 2, 3}, {4, 5, 6}};
        int[][] matriz3 = new int[][]{{1, 2, 3}, {4, 5, 6}};

        // Acceso a un elemento de una matriz
        System.out.println(matriz2[0][0]); // 1
        // Modificación de un elemento de una matriz
        matriz2[0][0] = 10;
        System.out.println(matriz2[0][0]); // 10

        // Iteración sobre una matriz
        for (int i = 0; i < matriz2.length; i++) {
            for (int j = 0; j < matriz2[i].length; j++) {
                System.out.println(matriz2[i][j]);
            }
        }

        // Iteración sobre una matriz con un bucle for-each
        for (int[] fila : matriz2) {
            for (int numero : fila) {
                System.out.println(numero);
            }
        }

        // Arrays de objetos
        String[] nombres = new String[3];
        nombres[0] = "Juan";
        nombres[1] = "María";
        nombres[2] = "Carlos";

        for (String nombre : nombres) {
            System.out.println(nombre);
        }

        // Métodos de la clase Arrays en Java
        int[] numeros4 = {5, 3, 2, 4, 1};
        Arrays.sort(numeros4);
        for (int numero : numeros4) {
            System.out.println(numero);
        }

        int[] numeros5 = {1, 2, 3, 4, 5};
        int[] numeros6 = {1, 2, 3, 4, 5};
        System.out.println(Arrays.equals(numeros5, numeros6)); // true

        int[] numeros7 = {1, 2, 3, 4, 5};
        int[] numeros8 = {1, 2, 3, 4, 6};
        System.out.println(Arrays.equals(numeros7, numeros8)); // false

        int[] numeros9 = {1, 2, 3, 4, 5};
        System.out.println(Arrays.toString(numeros9)); // [1, 2, 3, 4, 5]

        int[] numeros10 = {1, 2, 3, 4, 5};
        int[] numeros11 = Arrays.copyOf(numeros10, 3);
        System.out.println(Arrays.toString(numeros11)); // [1, 2, 3]

        int[] numeros12 = {1, 2, 3, 4, 5};
        int[] numeros13 = Arrays.copyOfRange(numeros12, 1, 4);
        System.out.println(Arrays.toString(numeros13)); // [2, 3, 4]

        int[] numeros14 = {1, 2, 3, 4, 5};
        Arrays.fill(numeros14, 0);
        System.out.println(Arrays.toString(numeros14)); // [0, 0, 0, 0, 0]

        int[] numeros15 = {1, 2, 3, 4, 5};
        int[] numeros16 = Arrays.copyOf(numeros15, numeros15.length);
        System.out.println(Arrays.equals(numeros15, numeros16)); // true
        
    }
}

