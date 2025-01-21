
public class Empleado {
	 	private static double pagoPorHoraExtra; //atributo de clase
	    private String nif;
	    private String nombre;
	    private double sueldoBase;
	    private int horasExtras;
	    private double tipoIRPF;
	    private char casado;  //S � N
	    private int numeroHijos;
	   
	    //Constructor por defecto
	    public Empleado() {
	    }

	    //Constructor con un par�metro
	    public Empleado(String nif) {
	        this.nif = nif;
	    }

	    //M�todos get/set
	    public char getCasado() {
	        return casado;
	    }

	    public void setCasado(char casado) {
	        this.casado = casado;
	    }

	    public int getHorasExtras() {
	        return horasExtras;
	    }

	    public void setHorasExtras(int horasExtras) {
	        this.horasExtras = horasExtras;
	    }

	    public String getNif() {
	        return nif;
	    }

	    public void setNif(String nif) {
	        this.nif = nif;
	    }

	    public String getNombre() {
	        return nombre;
	    }

	    public void setNombre(String nombre) {
	        this.nombre = nombre;
	    }

	    public int getNumeroHijos() {
	        return numeroHijos;
	    }

	    public void setNumeroHijos(int numeroHijos) {
	        this.numeroHijos = numeroHijos;
	    }

	    public double getSueldoBase() {
	        return sueldoBase;
	    }

	    public void setSueldoBase(double sueldoBase) {
	        this.sueldoBase = sueldoBase;
	    }

	    public double getTipoIRPF() {
	        return tipoIRPF;
	    }

	    public void setTipoIRPF(double tipoIRPF) {
	        this.tipoIRPF = tipoIRPF;
	    }

	    //m�todos get/set para el atributo static
	    public static double getPagoPorHoraExtra() {
	        return pagoPorHoraExtra;
	    }

	    public static void setPagoPorHoraExtra(double pagoPorHoraExtra) {
	        Empleado.pagoPorHoraExtra = pagoPorHoraExtra;
	    }
	   
	   
	    //calcular el importe de las horas extra
	    public double calcularImporteHorasExtras(){
	        return horasExtras * pagoPorHoraExtra;
	    }
	   
	    //calcular el sueldo bruto
	    public double calcularSueldoBruto(){
	        return sueldoBase + calcularImporteHorasExtras();
	    }
	   
	    //calcular el importe de las retencion por IRPF
	    public double calcularRetencionIrpf(){
	        double tipo = tipoIRPF;
	        if(casado == 's' || casado == 'S') {
	            tipo = tipo - 2; //2 puntos menos si est� casado
	        }
	        tipo = tipo - numeroHijos; //un punto menos por cada hijo                                                 
	        if(tipo<0){
	            tipo = 0;
	        }
	        return calcularSueldoBruto() * tipo / 100;
	    }
	   
	    //calcular el importe liquido a cobrar
	    public double calcularSueldo(){
	        return calcularSueldoBruto() - calcularRetencionIrpf();
	    }

	    //mostrar los datos de un trabajador
	    @Override
	    public String toString() {
	        StringBuilder sb = new StringBuilder();
	        sb.append("\nNif: ");
	        sb.append(nif);
	        sb.append("\nSueldo Base: ");
	        sb.append(sueldoBase);
	        sb.append("\nHoras Extras: ");
	        sb.append(horasExtras);
	        sb.append("\ntipo IRPF: ");
	        sb.append(tipoIRPF);
	        sb.append("\nCasado: ");
	        sb.append(casado);
	        sb.append("\nNúmero de Hijos: ");
	        sb.append(numeroHijos);
	        return  sb.toString();
	    }
	}//Fin de la Clase Empleado