import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static String findRecursive(char[][] raam, int x1, int x2, int y1, int y2) {

        if(x1 == x2 || y1 == y2) {
            return "";
        }

        boolean cutH = false;
        boolean cutV = false;
        int row = 0;
        int kol = 0;
        for (int x = x1+1; x < x2; x++) {

            boolean foundRow = true;

            for (int y = y1+1; y < y2; y++) {
                if(raam[x][y] != '*') {
                    foundRow = false;
                    break;
                }
            }

            if(foundRow) {
                row = x;
                cutH = true;
                break;
            }
        }

        if(cutH) {
            // Kolommen
            for(int y = y1+1; y < y2; y++) {

                boolean foundKol = true;
                // rijen
                for (int x = x1+1; x < x2; x++) {
                    if(raam[x][y] != '*') {
                        foundKol = false;
                        break;
                    }
                }

                if(foundKol) {
                    kol = y;
                    cutV = true;
                    break;
                }
            }
        }

        //System.out.println("Rij: " + row + " kolom: " + kol);

        if(cutH && cutV) {
            return String.format("(%d,%d)[%s][%s][%s][%s]", (row+1), (kol+1),
                    findRecursive(raam, x1, row, y1, kol),
                    findRecursive(raam, x1, row, kol, y2),
                    findRecursive(raam, row, x2, y1, kol),
                    findRecursive(raam, row, x2, kol, y2));
        } else {
            return "";
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);


        int amount = scanner.nextInt(); // aantal opgaven

        for(int i = 0; i < amount; i++) {
            int rijen = scanner.nextInt();
            int kolommen = scanner.nextInt();

            char[][] raam = new char[rijen][kolommen];

            // rijen
            for (int x = 0; x < rijen; x++) {
                raam[x] = scanner.next().toCharArray();
            }

            System.out.println(String.format("%d <%d,%d>%s", (i+1), rijen, kolommen, findRecursive(raam, 0, rijen, 0, kolommen)));
        }
    }
}
