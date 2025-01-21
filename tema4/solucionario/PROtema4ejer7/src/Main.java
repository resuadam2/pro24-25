import java.util.Scanner;

public class Main {
	   public static void main(String[] args) {
	        Scanner sc = new Scanner(System.in);
	        int d, m, a;

	        //Se pide por teclado el dia, mes y a�o
	        System.out.println("Introduce fecha: ");
	        System.out.print("dia: ");
	        d = sc.nextInt();
	        System.out.print("mes: ");
	        m = sc.nextInt();
	        System.out.print("anho: ");
	        a = sc.nextInt();

	        //Se crea un objeto Fecha utilizando el consructor con par�metros
	        Fecha fecha = new Fecha(d,m,a);

	        if (fecha.fechaCorrecta()) { //si la fecha es correcta

	           //Se muestra utilizando el m�todo toString()
	            System.out.println("Fecha introducida: " + fecha);

	            //Se muestran los 10 d�as siguientes utilizando el m�todo diaSiguiente()                              
	            System.out.println("Los 10 d�as siguientes son:");
	            for (int i = 1; i <= 10; i++) {
	                fecha.diaSiguiente();
	                System.out.println(fecha);
	            }

	        } else { //Si la fecha no es correcta
	            System.out.println("Fecha no valida");
	        }
	        sc.close();
	    }
}
