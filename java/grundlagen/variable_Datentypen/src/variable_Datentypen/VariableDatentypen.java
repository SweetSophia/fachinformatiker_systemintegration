package variable_Datentypen;

public class VariableDatentypen {

    public static void main(String[] args) {

        //Deklaration: Variable anlegen mit Datentyp und Bezeichner

        int ganzeZahl;
        long grosseGanzeZahl;
        double kommaZahl;
        char unicodeZeichen;
        boolean bool;

        //Initialisierung: Variable einen Wert zuweisen
        ganzeZahl = 28;
        grosseGanzeZahl = 19999999999999L;
        kommaZahl = 1.345;
        unicodeZeichen = 98;
        bool = true;

        //Deklaration und Initialisierung
        int ganzeZahl2 = 38;

        //Der Datentype String
        String zeichenkette = "ich bin eine Zeichenkette";

        System.out.println("Ganze Zahl: " + ganzeZahl);
        System.out.println("Addition: " + ganzeZahl + " " + ganzeZahl2);
        System.out.println("Ergebnis der Addition: " + (ganzeZahl + ganzeZahl2));

    }

}
