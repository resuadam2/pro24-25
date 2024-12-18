// Vamos a hablar sobre las Strings en Java

/**
 * Strings en Java
 * Las cadenas de caracteres en Java son objetos de la clase String.
 * A diferencia de otros lenguajes de programación, en Java las cadenas de caracteres son inmutables.
 * Esto significa que una vez que se crea una cadena de caracteres, no se puede modificar.
 * Si se necesita modificar una cadena de caracteres, se debe crear una nueva cadena de caracteres.
 * A pesar de esto, Java proporciona una serie de métodos para manipular cadenas de caracteres,
 * sin embargo, estos métodos no modifican la cadena de caracteres original, sino que devuelven una nueva cadena de caracteres.
 */
public class Main {
    public static void main(String[] args) {
        // Crear una cadena de caracteres
        String str = "Hola Mundo!";
        System.out.println(str);

        // Concatenar cadenas de caracteres
        String str1 = "Hola";
        String str2 = "Mundo!";
        String str3 = str1 + " " + str2;
        System.out.println(str3);

        // Longitud de una cadena de caracteres
        System.out.println(str.length());

        // Comparar cadenas de caracteres
        String str4 = "Hola";
        String str5 = "Hola";
        System.out.println(str4.equals(str5));

        // Comparar cadenas de caracteres ignorando mayúsculas y minúsculas
        String str6 = "Hola";
        String str7 = "hola";
        System.out.println(str6.equalsIgnoreCase(str7));

        // Obtener un carácter de una cadena de caracteres
        String str8 = "Hola";
        char ch = str8.charAt(0);
        System.out.println(ch);

        // Obtener la subcadena de una cadena de caracteres
        String str9 = "Hola Mundo!";
        String subStr = str9.substring(5);
        System.out.println(subStr);

        // Convertir una cadena de caracteres a minúsculas
        String str10 = "Hola Mundo!";
        String lowerStr = str10.toLowerCase();
        System.out.println(lowerStr);

        // Convertir una cadena de caracteres a mayúsculas
        String str11 = "Hola Mundo!";
        String upperStr = str11.toUpperCase();
        System.out.println(upperStr);

        // Eliminar espacios en blanco al principio y al final de una cadena de caracteres
        String str12 = " Hola Mundo! ";
        String trimmedStr = str12.trim();
        System.out.println(trimmedStr);

        // Reemplazar una subcadena de una cadena de caracteres
        String str13 = "Hola Mundo!";
        String replacedStr = str13.replace("Mundo", "Java");
        System.out.println(replacedStr);

        // Dividir una cadena de caracteres en subcadenas
        String str14 = "Hola Mundo!";
        String[] parts = str14.split(" "); // Dividir la cadena de caracteres en subcadenas utilizando el espacio como delimitador
        for (String part : parts) {
            System.out.println(part);
        }

        // Convertir un valor de otro tipo a una cadena de caracteres
        int num = 10;
        String str15 = String.valueOf(num);
        System.out.println(str15);

        // Convertir una cadena de caracteres a un valor de otro tipo
        String str16 = "10";
        int num2 = Integer.parseInt(str16);
        System.out.println(num2);

        // Formatear una cadena de caracteres
        String str17 = "Hola %s!";
        String formattedStr = String.format(str17, "Mundo");
        System.out.println(formattedStr);

        // Recorrer una cadena de caracteres
        String str18 = "Hola Mundo!";
        for (int i = 0; i < str18.length(); i++) {
            char x = str18.charAt(i);
            System.out.println(x);
        }

        /**
         * Sobre la clase StringBuilder:
         * La clase StringBuilder en Java se utiliza para crear cadenas de caracteres modificables.
         * A diferencia de la clase String, la clase StringBuilder es mutable, lo que significa que se puede modificar.
         * La clase StringBuilder proporciona una serie de métodos para manipular cadenas de caracteres.
         * Estos métodos modifican la cadena de caracteres original en lugar de devolver una nueva cadena de caracteres.
         * La clase StringBuilder es más eficiente que la clase String cuando se necesitan realizar muchas operaciones de modificación en una cadena de caracteres.
         * La clase StringBuilder es una clase no sincronizada, lo que significa que no es segura para subprocesos.
         * Si se necesita una cadena de caracteres mutable que sea segura para subprocesos, se debe utilizar la clase StringBuffer en lugar de la clase StringBuilder.
         * La clase StringBuffer es similar a la clase StringBuilder, pero es sincronizada, lo que significa que es segura para subprocesos.
         * Sin embargo, la clase StringBuffer es menos eficiente que la clase StringBuilder debido a la sincronización.
         * Por lo tanto, si no se necesita la sincronización, se debe utilizar la clase StringBuilder en lugar de la clase StringBuffer.
         * La clase StringBuilder se encuentra en el paquete java.lang y no es necesario importarla.
         * La clase StringBuilder tiene un constructor que acepta una cadena de caracteres como argumento y crea un objeto StringBuilder con el contenido de la cadena de caracteres.
         * La clase StringBuilder también tiene un constructor que acepta un entero como argumento y crea un objeto StringBuilder con una capacidad inicial especificada.
         * La capacidad de un objeto StringBuilder es el número de caracteres que puede contener sin tener que asignar más memoria.
         * La clase StringBuilder proporciona métodos para insertar, reemplazar, eliminar y revertir subcadenas en una cadena de caracteres.
         * Estos métodos modifican la cadena de caracteres original en lugar de devolver una nueva cadena de caracteres.
         */

        // Crear una cadena de caracteres con un constructor
        StringBuilder sb = new StringBuilder();
        sb.append("Hola");
        sb.append(" ");
        sb.append("Mundo!");
        String str19 = sb.toString();
        System.out.println(str19);

        // Crear una cadena de caracteres con un constructor y un tamaño inicial
        StringBuilder sb2 = new StringBuilder(20);
        sb2.append("Hola");
        sb2.append(" ");
        sb2.append("Mundo!");
        String str20 = sb2.toString();
        System.out.println(str20);

        // Insertar una subcadena en una cadena de caracteres
        StringBuilder sb3 = new StringBuilder("Hola Mundo!");
        sb3.insert(5, "Java ");
        String str21 = sb3.toString();
        System.out.println(str21);

        // Reemplazar una subcadena en una cadena de caracteres
        StringBuilder sb4 = new StringBuilder("Hola Mundo!");
        sb4.replace(5, 10, "Java");
        String str22 = sb4.toString();
        System.out.println(str22);

        // Eliminar una subcadena de una cadena de caracteres
        StringBuilder sb5 = new StringBuilder("Hola Mundo!");
        sb5.delete(5, 10);
        String str23 = sb5.toString();
        System.out.println(str23);

        // Eliminar todos los caracteres de una cadena de caracteres
        StringBuilder sb6 = new StringBuilder("Hola Mundo!");
        sb6.delete(0, sb6.length());
        String str24 = sb6.toString();
        System.out.println(str24);

        // Invertir una cadena de caracteres
        StringBuilder sb7 = new StringBuilder("Hola Mundo!");
        sb7.reverse();
        String str25 = sb7.toString();
        System.out.println(str25);
    }
}