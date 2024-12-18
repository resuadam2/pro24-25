/**
 * Vamos a ver las diferentes estructuras de control que podemos utilizar en Java.
 * Las estructuras de control nos permiten controlar el flujo de ejecución de un programa.
 * Vamos a ver las estructuras de control secuencial, condicional y repetitiva.
 */
public class Main {
    public static void main(String[] args) {
        /**
         * 1. Estructuras de control de flujo
         * Las estructuras de control de flujo nos permiten controlar el flujo de ejecución de un programa.
         */
        // 1.1. Estructura de control secuencial
        // La estructura de control secuencial es la que se ejecuta de arriba hacía abajo.
        System.out.println("Estructura de control secuencial");
        System.out.println("Primera línea");
        System.out.println("Segunda línea");
        System.out.println("Tercera línea");

        // 1.2. Estructura de control condicional
        // La estructura de control condicional nos permite ejecutar un bloque de código si se cumple una condición.
        System.out.println("\nEstructura de control condicional");
        int num = 10;
        if (num > 0) {
            System.out.println("El número es positivo");
        }

        // Cuándo se cumple la condición se ejecuta el bloque de código, en caso contrario no se ejecuta.
        if (num < 0) {
            System.out.println("El número es negativo");
        }

        // Se pueden escribir también en una sola línea
        if (num == 0) System.out.println("El número es cero");

        // Podemos añadir un bloque de código que se ejecutará si no se cumple la condición
        if (num < 0) {
            System.out.println("El número es negativo");
        } else {
            System.out.println("El número no es negativo");
        }

        // También podemos añadir más condiciones

        // Si el número es positivo
        if (num > 0) {
            System.out.println("El número es positivo");
            // Si el número es negativo
        } else if (num < 0) {
            System.out.println("El número es negativo");
            // Si el número es cero
        } else {
            System.out.println("El número es cero");
        }

        // Existen dos operadores lógicos que nos permiten combinar condiciones
        // 1. Operador AND (&&)
        // Se cumple si ambas condiciones son verdaderas
        if (num > 0 && num < 100) {
            System.out.println("El número es positivo y menor que 100");
        }

        // 2. Operador OR (||)
        // Se cumple si al menos una de las condiciones es verdadera
        if (num < 0 || num > 100) {
            System.out.println("El número es negativo o mayor que 100");
        }

        // También podemos crear una estructura de control condicional según un valor
        String dia = "lunes";
        switch (dia) {
            case "lunes":
                System.out.println("Hoy es lunes");
                break;
            case "martes":
                System.out.println("Hoy es martes");
                break;
            case "miércoles":
                System.out.println("Hoy es miércoles");
                break;
            case "jueves":
                System.out.println("Hoy es jueves");
                break;
            case "viernes":
                System.out.println("Hoy es viernes");
                break;
            case "sábado":
                System.out.println("Hoy es sábado");
                break;
            case "domingo":
                System.out.println("Hoy es domingo");
                break;
            default:
                System.out.println("No es un día de la semana");
        }

        // Esta estructura también se puede escribir de la siguiente forma
        switch (dia) {
            case "lunes" -> System.out.println("Hoy es lunes");
            case "martes" -> System.out.println("Hoy es martes");
            case "miércoles" -> System.out.println("Hoy es miércoles");
            case "jueves" -> System.out.println("Hoy es jueves");
            case "viernes" -> System.out.println("Hoy es viernes");
            case "sábado" -> System.out.println("Hoy es sábado");
            case "domingo" -> System.out.println("Hoy es domingo");
            default -> System.out.println("No es un día de la semana");
        }

        // 1.3. Estructura de control repetitiva
        // La estructura de control repetitiva nos permite ejecutar un bloque de código varias veces.
        System.out.println("\nEstructura de control repetitiva");

        // 1.3.1. Bucle while
        // El bucle while ejecuta un bloque de código mientras se cumpla una condición
        int contador = 0;
        while (contador < 5) {
            System.out.println("Contador: " + contador);
            contador++;
        }

        // 1.3.2. Bucle do-while
        // El bucle do-while ejecuta un bloque de código al menos una vez y después comprueba si se cumple una condición
        contador = 0;
        do {
            System.out.println("Contador: " + contador);
            contador++;
        } while (contador < 5);

        // 1.3.3. Bucle for
        // El bucle for ejecuta un bloque de código un número determinado de veces
        for (int i = 0; i < 5; i++) {
            System.out.println("Contador: " + i);
        }

        // También podemos recorrer un array con un bucle for
        int[] numeros = {1, 2, 3, 4, 5};
        for (int i = 0; i < numeros.length; i++) {
            System.out.println("Número: " + numeros[i]);
        }

        // Otra forma de recorrer un array con un bucle for mejorado o for-each
        for (int numero : numeros) {
            System.out.println("Número: " + numero);
        }

        // 1.3.4. Bucle for anidado
        // Podemos anidar bucles for
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.println("i: " + i + ", j: " + j);
            }
        }

        // 1.3.5. Bucle for-each anidado
        // También podemos anidar bucles for-each
        int[][] matriz = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        for (int[] fila : matriz) {
            for (int numero : fila) {
                System.out.println("Número: " + numero);
            }
        }

        // 1.3.6. Bucle infinito
        // Podemos crear un bucle infinito con la instrucción while(true)
        //while (true) {
        //    System.out.println("Bucle infinito");
        //}

        // 1.3.7. Interrumpir un bucle
        // Podemos interrumpir un bucle con la instrucción break
        for (int i = 0; i < 5; i++) {
            if (i == 3) {
                break;
            }
            System.out.println("Contador: " + i);
        }

        // 1.3.8. Saltar una iteración
        // Podemos saltar una iteración con la instrucción continue
        for (int i = 0; i < 5; i++) {
            if (i == 3) {
                continue;
            }
            System.out.println("Contador: " + i);
        }

        // 1.3.9. Etiquetas
        // Podemos utilizar etiquetas para identificar un bucle, esto nos permite interrumpir un bucle anidado
        etiqueta: for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 3; j++) {
                if (j == 2) {
                    break etiqueta;
                }
                System.out.println("i: " + i + ", j: " + j);
            }
        }

        // Podemos utilizar etiquetas también con la instrucción continue
        etiqueta: for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 3; j++) {
                if (j == 2) {
                    continue etiqueta;
                }
                System.out.println("i: " + i + ", j: " + j);
            }
        }

        // También podemos escribir un bucle en una sola línea
        for (int i = 0; i < 5; i++) System.out.println("Contador: " + i);

        // Otra forma de escribir un bucle en una sola línea
        for (int i = 0; i < 5; i++) System.out.print(i + " ");

    }
}