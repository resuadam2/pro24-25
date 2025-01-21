
public class Asiento {
	 /*Atributos*/
    private char letra;
    private int fila;
    private Espectador espectador; // informacion del espectador que esta sentado, null si es vacio
 
    /*Constructores*/
    public Asiento(char letra, int fila) {
        this.letra = letra;
        this.fila = fila;
        this.espectador = null; //al iniciar el asiento, no habr� nadie sentado
    }
 
    /*Metodos*/
    public char getLetra() {
        return letra;
    }
 
    public void setLetra(char letra) {
        this.letra = letra;
    }
 
    public int getFila() {
        return fila;
    }
 
    public void setFila(int fila) {
        this.fila = fila;
    }
 
    public Espectador getEspectador() {
        return espectador;
    }
 
    public void setEspectador(Espectador espectador) {
        this.espectador = espectador;
    }
 
    /**
     * Indica si el asiento esta ocupado
     *
     * @return
     */
    public boolean ocupado() {
        return espectador != null;
    }
 
    @Override
    public String toString() {
        if (ocupado()) {
            return "Asiento: " + fila + letra + " y " + espectador;
        }
 
        return "Asiento: " + fila + letra + " y este asiento est� vacio ";
 
    }
}
