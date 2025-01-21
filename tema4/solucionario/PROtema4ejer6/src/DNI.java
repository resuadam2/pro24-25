import java.util.Scanner;

public class DNI {
    private int dni;
    private char letra;

    //Constructores
    public DNI() {
    }

    public DNI(int dni) {
        this.dni = dni;
        letra = calcularLetra();
    }

    //Método para calcular la letra del NIF
    private char calcularLetra() {
        char[] letras = {'T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X',
                                'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E'};                      
        return letras[dni % 23];
    }

    //Método para leer por teclado el número de DNI y calcular la letra
    public void leer() {
        Scanner sc = new Scanner(System.in);
        do {
            System.out.print("Introduce dni: ");
            dni = sc.nextInt();
        } while (dni <= 0);
        letra = calcularLetra();
        sc.close();
    }

    //Método que devuelve un String de la forma 99999999-X
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(dni);
        sb.append("-");
        sb.append(letra);
        return sb.toString();
    }


}
