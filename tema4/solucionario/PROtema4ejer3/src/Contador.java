
public class Contador {

    private int cont;

    //constructor por defecto
    public Contador() {
    }

    //constructor con par�metros
    public Contador(int cont) {
        if (cont < 0) {
            this.cont = 0;
        } else {
            this.cont = cont;
        }
    }

    //getter
    public int getCont() {
        return cont;
    }

    //setter
    public void setCont(int cont) {
        if (cont < 0) {
            this.cont = 0;
        } else {
            this.cont = cont;
        }
    }

    //m�todo incrementar contador
    public void incrementar() {
        cont++;
    }

    //m�todo decrementar contador
    public void decrementar() {
        cont--;
        if (cont < 0) {
            cont = 0;
        }
    }
}//Fin de la clase Contador