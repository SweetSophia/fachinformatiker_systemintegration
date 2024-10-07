package variable_Datentypen;

public class Operatoren {

    public static void main(String[] args) {

        int x = 1;
        int y = 2;

        //arithmetische Operatoren
        int summe = x + y;  //5
        int differenz = x - y;  //1
        int produkt = x * y;   //6
        int quotient = x / y;   //1, weil x und y int sind
        double quotientD = x / y;   //1.0

        System.out.println(quotient);

        //Modulo Operator (Ganzzahliger Rest einer Division)
		/*Scanner scan = new Scanner(System.in);
		System.out.print("Bitte Zahl1 eingeben: ");
		int zahl1 = scan.nextInt();

		System.out.print("Bitte Zahl2 eingeben: ");
		int zahl2 = scan.nextInt();

		System.out.println("Division " + (zahl1 / zahl2));
		System.out.println("Rest " + (zahl1 % zahl2));	*/

        //Inkrement- und Dekrementoperator (++ und --)

        //Postfix-Notation
        int inkr = 10;
        inkr++;
        System.out.println(inkr);

        //Präfix-Notation
        --inkr;
        System.out.println(inkr);

        //relationale Operatoren
        int zahl3 = 10;

        System.out.println(zahl3 < 20);   //true
        System.out.println(zahl3 >= 20);  //false
        System.out.println(zahl3 == 10);  //true
        System.out.println(zahl3 != 10);

    }

}
