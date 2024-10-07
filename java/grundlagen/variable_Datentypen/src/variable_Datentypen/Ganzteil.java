package variable_Datentypen;

import java.util.Scanner;
// Alternativ: java.util.*

public class Ganzteil {

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);

        System.out.print("Dividend: ");
        int dividend = scan.nextInt();

        System.out.print("Divisor: ");
        int divisor = scan.nextInt();

        System.out.println("Das Ergebnis der Division " + dividend + ":" + divisor + " ist "
                + (dividend/divisor) +" Rest " + (dividend % divisor));

        scan.close();

    }
}
