import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files
import java.util.Arrays;
import java.lang.Math;

public class Main {
    public static void main(String[] args) {

        int[] expenses = {0};

        try {
            // Hent expense report
            File myObj = new File("Expenses.txt");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                expenses = Arrays.copyOf(expenses,expenses.length + 1);
                expenses[expenses.length - 1] = Integer.parseInt(data);

            }
            myReader.close();

            // Sorter expense report
            Arrays.sort(expenses);



            /* Blokk for del 1
            for (int i = 0; i < Math.ceil((expenses.length - 1)/2); i++) {
                int posisjon = expenses.length; // posisjonen til tallet som legges til tall nr i
                int sum = 2021; // Summen av elementene som legges sammen, skal bli 2020
                while (sum > 2020) {
                    posisjon--;
                    sum = expenses[i] + expenses[posisjon];
                    System.out.println(sum);
                    if (sum == 2020){
                        System.out.println(expenses[i]);
                        System.out.println(expenses[posisjon]);
                    }
                }
                if (sum == 2020){
                    System.out.println(expenses[i] * expenses[posisjon]);
                    break;
                }
            }
            */

            // Del 2
            for (int i = 1; i < Math.ceil((expenses.length - 1)/2); i++) {
                int posisjon = expenses.length; // posisjonen til det første tallet som legges til tall nr i
                int pos2 = i;// posisjonen til det andre tallet som legges til tall nr i
                int sum = 2021; // Summen av elementene som legges sammen, skal bli 2020
                while (sum > 2020) {
                    pos2++;
                    while (sum > 2020) {
                        posisjon--;
                        sum = expenses[i] + expenses[posisjon] + expenses[pos2];
                        System.out.println(sum);
                        if (sum == 2020) {
                            System.out.println(expenses[i]);
                            System.out.println(expenses[posisjon]);
                            System.out.println(expenses[pos2]);
                        }
                    }
                }
                if (sum == 2020){
                    System.out.println(expenses[i] * expenses[posisjon] * expenses[pos2]);
                    break;
                }
            }



        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }
}