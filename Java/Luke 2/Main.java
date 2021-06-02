import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files
import java.util.Arrays;
import java.lang.Math;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {

        ArrayList<String> info = new ArrayList<>();

        try {
            // Hent expense report
            File myObj = new File("passwords.txt");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                info.add(data);

            }
            myReader.close();

            // Del 1
            /*
            int correctPasswords = 0;


            for (String i : info) {
                String[] split1 = i.split(":"); // Del opp i info og passord
                String password = split1[1];
                char occuringLetter = split1[0].charAt(split1[0].length() - 1);
                String[] split2 = split1[0].split("-");
                int minOccurences = Integer.parseInt(split2[0]);
                String[] split3 = split2[1].split(" ");
                int maxOccurences = Integer.parseInt(split3[0]);

                int occurences = countOccurences(password, occuringLetter);
                if ((occurences <= maxOccurences) && (occurences >= minOccurences)) {
                    correctPasswords++;
                }
            }

            System.out.println(correctPasswords);

             */

            // Del 2

            int correctPasswords = 0;

            for (String i : info) {
                String[] split1 = i.split(":"); // Del opp i info og passord
                String password = split1[1];
                char occuringLetter = split1[0].charAt(split1[0].length() - 1);
                String[] split2 = split1[0].split("-");
                int minOccurences = Integer.parseInt(split2[0]);
                String[] split3 = split2[1].split(" ");
                int maxOccurences = Integer.parseInt(split3[0]);

                if ((password.charAt(maxOccurences) == occuringLetter) && (password.charAt(minOccurences) != occuringLetter)) {
                    correctPasswords++;
                } else if ((password.charAt(minOccurences) == occuringLetter) && (password.charAt(maxOccurences) != occuringLetter)) {
                    correctPasswords++;
                }
            }
            System.out.println(correctPasswords);

        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }

    public static int countOccurences(String word, char letter) {
        int count = 0;
        for (int i = 0; i < word.length(); i++) {
            if (word.charAt(i) == letter) {
                count++;
            }
        }
        return count;
    }
}
