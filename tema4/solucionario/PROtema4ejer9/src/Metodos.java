
public class Metodos {
	 public static final String nombres[] = {"Fernando", "Laura", "Pepe", "Eufrasio"};
	 
	    public static int generaNumeroEnteroAleatorio(int minimo, int maximo) {
	        int num = (int) (Math.random() * (minimo - (maximo + 1)) + (maximo + 1));
	        return num;
	    }
}
