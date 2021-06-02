import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files
import java.util.ArrayList;


public class Main {
    public static void main(String[] args) {

        ArrayList<String> info = new ArrayList<>();

        try {
            // Hent info
            File myObj = new File("passports.txt");
            Scanner myReader = new Scanner(myObj);
            String passport = " ";
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();

                if (data.length() < 2){
                    info.add(passport);
                    passport = " ";
                    continue;
                } else {
                    passport = passport + " " + data;
                }
            }
            myReader.close();

            /* Del 1
            int validPassports = 0;

            String[] fields = {"byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:", "cid:"};


            for (String i : info) {
                int presentFields = 0;
                System.out.println(i);
                for (int j = 0; j < fields.length - 1; j++){
                    if (i.contains(fields[j])){
                        presentFields++;
                    } else {
                        break;
                    }
                }
                if (presentFields == 7){
                    validPassports++;
                }
            }
            System.out.println(validPassports);

             */

            // Del 2

            int validPassports = 0;

            for (String i : info) {
                int validFields = 0;
                System.out.println(i);

                if (i.contains("byr:")){
                    int byrPos = i.indexOf("byr:");
                    String[] remainder = i.substring(byrPos+4, i.length()).split(" ");
                    int byr = Integer.parseInt(remainder[0]);
                    if ((byr >= 1920) && byr <= 2002){
                        validFields++;
                    }
                    System.out.println(validFields);
                } else {
                    continue;
                }

                if (i.contains("iyr:")){
                    int iyrPos = i.indexOf("iyr:");
                    String[] remainder = i.substring(iyrPos+4, i.length()).split(" ");
                    int iyr = Integer.parseInt(remainder[0]);
                    if ((iyr >= 2010) && iyr <= 2020){
                        validFields++;
                    }
                    System.out.println(validFields);
                } else {
                    continue;
                }

                if (i.contains("eyr:")){
                    int eyrPos = i.indexOf("eyr:");
                    String[] remainder = i.substring(eyrPos+4, i.length()).split(" ");
                    int eyr = Integer.parseInt(remainder[0]);
                    if ((eyr >= 2020) && eyr <= 2030){
                        validFields++;
                    }
                    System.out.println(validFields);
                } else {
                    continue;
                }

                if (i.contains("hgt:")){
                    int hgtPos = i.indexOf("hgt:");
                    String[] remainder = i.substring(hgtPos+4, i.length()).split(" ");
                    if (remainder[0].contains("cm")) {
                        String[] height = remainder[0].split("c");
                        int hgt = Integer.parseInt(height[0]);
                        if ((hgt >= 150) && hgt <= 193){
                            validFields++;
                        }
                    }
                    if (remainder[0].contains("in")) {
                        String[] height = remainder[0].split("i");
                        int hgt = Integer.parseInt(height[0]);
                        if ((hgt >= 59) && hgt <= 76){
                            validFields++;
                        }
                    }

                    System.out.println(validFields);
                } else {
                    continue;
                }

                if (i.contains("hcl:")){
                    int hclPos = i.indexOf("hcl:");
                    String[] remainder = i.substring(hclPos+4, i.length()).split(" ");
                    String hcl = remainder[0];
                    if (hcl.length() == 7){
                        if (hcl.charAt(0) == '#') {
                            int validChars = 0;
                            for (int k = 1; k < hcl.length(); k++){
                                int ascii = (int) hcl.charAt(k);
                                if (((ascii >= 48) && (ascii <= 57)) || ((ascii >= 97) && (ascii <= 122))){
                                    validChars++;
                                } else {
                                    break;
                                }
                            }
                            if (validChars == 6){
                                validFields++;
                            }
                        }
                    }
                    System.out.println(validFields);
                } else {
                    continue;
                }

                if (i.contains("ecl:")){
                    int eclPos = i.indexOf("ecl:");
                    String[] remainder = i.substring(eclPos+4, i.length()).split(" ");
                    String ecl = remainder[0];

                    String[] acceptableEcl = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"};
                    for (String m : acceptableEcl){
                        if (ecl.equals(m)){
                            validFields++;
                        }
                    }
                    System.out.println(validFields);
                } else {
                    continue;
                }

                if (i.contains("pid:")){
                    int pidPos = i.indexOf("pid:");
                    String[] remainder = i.substring(pidPos+4, i.length()).split(" ");
                    String pid = remainder[0];

                    int validNumbers = 0;
                    if (pid.length() == 9){
                        for (int n = 0; n < pid.length(); n++){
                            int ascii = (int) pid.charAt(n);
                            if ((ascii >= 48) && (ascii <= 57)){
                                validNumbers++;
                            } else {
                                break;
                            }
                        }
                        if (validNumbers == 9){
                            validFields++;
                        }
                    }


                    System.out.println(validFields);
                } else {
                    continue;
                }

                String[] fields = {"pid:", "cid:"};

                if (validFields == 7){
                    validPassports++;
                }
            }
            System.out.println(validPassports);



        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }

}