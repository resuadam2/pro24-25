
public class Main {
		public static void main(String[] args) {                                                  
	        // Se crean 4 fracciones
	        Fraccion f1 = new Fraccion(1, 4); // Fracci�n 1/4
	        Fraccion f2 = new Fraccion(1, 2); // Fracci�n 1/2
	        Fraccion f3 = new Fraccion(); // Fracci�n 0/1
	        Fraccion f4 = new Fraccion(4); // Fracci�n 4/1
	        // operaciones aritm�ticas con esas fracciones
	        Fraccion suma = f1.sumar(f2);
	        Fraccion resta = f1.restar(f3);
	        Fraccion producto = f1.multiplicar(f4);
	        Fraccion cociente = f1.dividir(f2);
	        //mostrar resultados
	        System.out.println(f1 + " + " + f2 + " = " + suma);
	        System.out.println(f1 + " - " + f3 + " = " + resta);
	        System.out.println(f1 + " * " + f4 + " = " + producto);
	        System.out.println(f1 + " / " + f2 + " = " + cociente);                                                   
	}
}
