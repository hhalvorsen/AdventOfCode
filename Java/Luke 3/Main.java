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
            // Hent info
            File myObj = new File("trees.txt");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                info.add(data);

            }
            myReader.close();

            // Del 2

            int treesHit = 0;
            int down = 2;
            int right = 1;
            int hPos = 0;
            int boardWidth = info.get(0).length();

            for (int i = down; i < info.size(); i = i + down) {
                String line = info.get(i);
                hPos = (hPos + right)%boardWidth;
                if (line.charAt(hPos) == '#') {
                    treesHit++;
                }
            }
            System.out.println(treesHit);

            long result = 84 * 289 * 89 * 71 * 36;
            System.out.println(Long.toString(result));



        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }

}
