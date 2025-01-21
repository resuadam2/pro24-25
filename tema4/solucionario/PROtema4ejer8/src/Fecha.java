public class Fecha {

    private int dia;
    private int mes;
    private int anho;

    //Constructor por defecto
    public Fecha() {
    }

    //Constructor con parnhmetros
    public Fecha(int dia, int mes, int anho) {
        this.dia = dia;
        this.mes = mes;
        this.anho = anho;
    }

    //Mnhtodos get y set
    public void setDia(int d) {
        dia = d;
    }

    public void setMes(int m) {
        mes = m;
    }

    public void setAnho(int a) {
        anho = a;
    }

    public int getDia() {
        return dia;
    }

    public int getMes() {
        return mes;
    }

    public int getAnho() {
        return anho;
    }

    //Comprobar si la fecha es correcta
    public boolean fechaCorrecta() {
        boolean diaCorrecto, mesCorrecto, anhoCorrecto;
        anhoCorrecto = anho > 0;
        mesCorrecto = mes >= 1 && mes <= 12;
        switch (mes) {
            case 2:
                if (esBisiesto()) {
                    diaCorrecto = dia >= 1 && dia <= 29;
                } else {
                    diaCorrecto = dia >= 1 && dia <= 28;
                }
                break;
            case 4:
            case 6:
            case 9:
            case 11:
                diaCorrecto = dia >= 1 && dia <= 30;
                break;
            default:
                diaCorrecto = dia >= 1 && dia <= 31;
        }
        return diaCorrecto && mesCorrecto && anhoCorrecto;
    }

    //Comprobar si el anho es bisiesto
    //Mnhtodo privado invocado desde el mnhtodo fechaCorrecta
    private boolean esBisiesto() {
        return (anho % 4 == 0 && anho % 100 != 0 || anho % 400 == 0);
    }

    public void diaSiguiente() {
        dia++;
        if (!fechaCorrecta()) {
            dia = 1;
            mes++;
            if (!fechaCorrecta()) {
                mes = 1;
                anho++;
            }

        }
    }

    //Mnhtodo para comprobar si la fecha es mayor que la que se recibe                                             
    public boolean esMayorQue(Fecha f){
        if(anho > f.anho) {
            return true;
        }
        else if(anho==f.anho && mes > f.mes) {
            return true;
        }
        else if(anho==f.anho && mes == f.mes && dia > f.dia) {
            return true;
        }
        return false;
    }
   
    //Mnhtodo para mostrar la fecha
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        if (dia < 10) {
            sb.append("0");
        }
        sb.append(dia);
        sb.append("-");
        if (mes < 10) {
            sb.append("0");
        }
        sb.append(mes);
        sb.append("-");

        sb.append(anho);
        return sb.toString();
    }
} //Final de la Clase Fecha