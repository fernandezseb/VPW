import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);


        double amount = scanner.nextDouble(); // aantal opgaven
        for(int i = 0; i < amount; i++) {

            double input = scanner.nextDouble();
            int count = 1;
            double max = input;


            while (input > 0) {

                if (input > max ) {
                    max = input;
                }

                input = scanner.nextDouble();
                count++;

                //System.out.prdoubleln(count);
            }
            count -= 1;


            double estimate = (((count + 1) * max) / count) - 1;
            System.out.println((i+1) + " " + (int)Math.round(estimate));

        }
    }

}
