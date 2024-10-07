package variable_Datentypen;

import java.util.Scanner;
//Alternativ import java.util.*;

public class EinlesenKonsole {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.println("Bitte Name eingeben: ");
        String name = input.nextLine();

        System.out.println("Bitte Alter eingeben: ");
        int alter = input.nextInt(); //erwartet integer - bei allem anderen abbruch

        System.out.println("Guten Tag, Benutzer " + name);
        System.out.println("Benutzer " + name + " ist " + alter + " Jahre alt");

        input.close();

    }

}
