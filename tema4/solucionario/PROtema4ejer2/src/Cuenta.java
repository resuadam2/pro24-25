
public class Cuenta {
	   private String nombre;
	    private String numeroCuenta;
	    private double tipoInteres;
	    private double saldo;

	    //Constructor por defecto
	    public Cuenta() {
	    }

	    //Constructor con parámetros
	    public Cuenta(String nombre, String numeroCuenta, double tipoInteres, double saldo) {                         
	        this.nombre = nombre;
	        this.numeroCuenta = numeroCuenta;
	        this.tipoInteres = tipoInteres;
	        this.saldo = saldo;
	    }

	    //Constructor copia
	    public Cuenta(final Cuenta c) {
	        nombre = c.nombre;
	        numeroCuenta = c.numeroCuenta;
	        tipoInteres = c.tipoInteres;
	        saldo = c.saldo;
	    }

	    //getters y setters
	    public void setNombre(String s) {
	        nombre = s;
	    }

	    public void setNumeroCuenta(String s) {
	        numeroCuenta = s;
	    }

	    public void setTipoInteres(double n) {
	        tipoInteres = n;
	    }

	    public void setSaldo(double n) {
	        saldo = n;
	    }

	    public String getNombre() {
	        return nombre;
	    }

	    public String getNumeroCuenta() {
	        return numeroCuenta;
	    }

	    public double getTipoInteres() {
	        return tipoInteres;
	    }

	    public double getSaldo() {
	        return saldo;
	    }

	    //método ingreso
	    public boolean ingreso(double n) {
	        boolean ingresoCorrecto = true;
	        if (n < 0) {
	            ingresoCorrecto = false;
	        } else {
	            saldo = saldo + n;
	        }
	        return ingresoCorrecto;
	    }

	    //método reintegro
	    public boolean reintegro(double n) {
	        boolean reintegroCorrecto = true;                                                                         
	        if (n < 0) {
	            reintegroCorrecto = false;
	        } else if (saldo >= n) {
	            saldo -= n;
	        } else {
	            reintegroCorrecto = false;
	        }
	        return reintegroCorrecto;
	    }

	    //método transferencia
	    public boolean transferencia(Cuenta c, double n) {
	        boolean correcto = true;
	        if (n < 0) {
	            correcto = false;
	        } else if (saldo >= n) {
	            reintegro(n);
	            c.ingreso(n);
	        } else {
	            correcto = false;
	        }
	        return correcto;
	    }
}
