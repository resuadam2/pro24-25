
//Clase Principal
import java.io.IOException;
import java.util.Scanner;

public class Main {

    final static int MAXIMO_EMPLEADOS = 20;
    static Empleado[] empleados = new Empleado[MAXIMO_EMPLEADOS];
    static int indice = 0;
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) throws IOException {

        double importe;
        Empleado e;
        leerEmpleados();
        if (numeroDeEmpleados() > 0) {

            //mostrar empleados
            System.out.println("\n\nEmpleados introducidos: ");
            mostrar();

            importe = leerImporteHorasExtras();

            //asignar el atributo est�tico pagoPorHoraExtra
            Empleado.setPagoPorHoraExtra(importe);

            //calcular el empleado que m�s cobra
            e = empleadoQueMasCobra();
            System.out.println("\n\nEmpleado que más cobra:");
            System.out.println(e);
            System.out.printf("Sueldo: %.2f € %n", e.calcularSueldo());

            //calcular el empleado que menos cobra
            e = empleadoQueMenosCobra();
            System.out.println("\n\nEmpleado que menos cobra:");
            System.out.println(e);
            System.out.printf("Sueldo: %.2f € %n", e.calcularSueldo());

            //calcular el empleado que m�s cobra por horas extra
            e = empleadoQueMasCobraPorHorasExtras();
            System.out.println("\n\nEmpleado que más cobra por horas extras:");
            System.out.println(e);
            System.out.printf("Total horas extras: %.2f €" , e.calcularImporteHorasExtras());

            //calcular el empleado que menos cobra por horas extra
            e = empleadoQueMenosCobraPorHorasExtras();
            System.out.println("\n\nEmpleado que menos cobra por horas extras:");
            System.out.println(e);
            System.out.printf("Total horas extras: %.2f €" , e.calcularImporteHorasExtras());

            //ordenar por salario de menor a mayor
            ordenarPorSalario();
            System.out.println("\n\nEmpleados ordenados por salario:");
            mostrarEmpleadosYSalarios();

        }
    }

    //m�todo para leer todos los empleados y guardarlos en el array
    public static void leerEmpleados() throws IOException {
        Empleado e;
        String dni, nombre;
        double sueldoBase;
        int horasExtras;
        double tipoIRPF;
        char casado;  // S � N
        int numeroHijos;
        int i, N;

        do {
            System.out.print("N�mero de empleados? ");
            N = sc.nextInt();
        } while (N < 0 || N > MAXIMO_EMPLEADOS);
       
        for (i = 1; i <= N; i++) {
            sc.nextLine(); //limpiar el intro
            System.out.println("Empleado " + i);
            System.out.print("Nif: ");
            dni = sc.nextLine();
            System.out.print("Nombre: ");
            nombre = sc.nextLine();
            System.out.print("Sueldo Base: ");
            sueldoBase = sc.nextDouble();
            System.out.print("Horas extra: ");
            horasExtras = sc.nextInt();
            System.out.print("Tipo de IRPF: ");
            tipoIRPF = sc.nextDouble();
            System.out.print("Casado (S/N): ");
            casado = (char) System.in.read();
            System.out.print("Número de hijos: ");
            numeroHijos = sc.nextInt();

            e = new Empleado(dni); //crear una nueva instancia de empleado

            e.setNombre(nombre);
            e.setSueldoBase(sueldoBase);
            e.setHorasExtras(horasExtras);
            e.setTipoIRPF(tipoIRPF);
            e.setCasado(Character.toUpperCase(casado));
            e.setNumeroHijos(numeroHijos);

            empleados[indice] = e; //se a�ade el empleado al array
            indice++;
        }
    }

    //m�todo para mostrar todos los empleados
    public static void mostrar() {
        for (int i = 0; i < indice; i++) {
            System.out.println(empleados[i]);
        }
    }

    //m�todo para pedir el importe de la hora extra
    public static double leerImporteHorasExtras() {
        double importe;
        System.out.print("Introduce el importe a pagar por cada hora extra: ");
        importe = sc.nextDouble();
        return importe;
    }

    //m�todo que devuelve el n�mero total de empleados
    public static int numeroDeEmpleados() {
        return indice;
    }

    //m�todo que devuelve el empleado que m�s cobra
    public static Empleado empleadoQueMasCobra() {
        Empleado mayor = empleados[0];
        for (int i = 1; i < indice; i++) {
            if (empleados[i].calcularSueldo() > mayor.calcularSueldo()) {
                mayor = empleados[i];
            }
        }
        return mayor;
    }

    //m�todo que devuelve el empleado que menos cobra
    public static Empleado empleadoQueMenosCobra() {
        Empleado menor = empleados[0];
        for (int i = 1; i < indice; i++) {
            if (empleados[i].calcularSueldo() < menor.calcularSueldo()) {
                menor = empleados[i];
            }
        }
        return menor;
    }

    //m�todo que devuelve el empleado que m�s cobra por horas extra
    public static Empleado empleadoQueMasCobraPorHorasExtras() {
        Empleado mayor = empleados[0];
        for (int i = 1; i < indice; i++) {
            if (empleados[i].calcularImporteHorasExtras() > mayor.calcularImporteHorasExtras()) {
                mayor = empleados[i];
            }
        }
        return mayor;
    }

    //m�todo que devuelve el empleado que menos cobra por horas extra
    public static Empleado empleadoQueMenosCobraPorHorasExtras() {
        Empleado menor = empleados[0];
        for (int i = 1; i < indice; i++) {
            if (empleados[i].calcularImporteHorasExtras() < menor.calcularImporteHorasExtras()) {                 
                menor = empleados[i];
            }
        }
        return menor;
    }

    //m�todo para ordenar todos los empleados por su salario de menor a mayor
    public static void ordenarPorSalario() {

        int i, j;
        Empleado aux;
        for (i = 0; i < indice - 1; i++) {
            for (j = 0; j < indice - i - 1; j++) {
                if (empleados[j + 1].calcularSueldo() < empleados[j].calcularSueldo()) {
                    aux = empleados[j + 1];
                    empleados[j + 1] = empleados[j];
                    empleados[j] = aux;
                }
            }
        }
    }

    //m�todo para mostrar los datos de cada empleado junto con su sueldo
    public static void mostrarEmpleadosYSalarios() {
        for (int i = 0; i < indice; i++) {
            System.out.println(empleados[i]);
            System.out.printf("Sueldo: %.2f � %n" , empleados[i].calcularSueldo());
        }
    }
}//Fin de la Clase Principal