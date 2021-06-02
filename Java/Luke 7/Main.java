import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files
import java.util.ArrayList;


public class Main {
    public static void main(String[] args) {

        ArrayList<Bag> mainBags = new ArrayList<>();

        try {
            // Hent info
            File myObj = new File("input.txt");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String input = myReader.nextLine();
                String[] tempLine = input.split(" ");

                Bag tempBag = new Bag();
                tempBag.colour = (tempLine[0] + " " + tempLine[1]);

                for (int i = 5; i < tempLine.length - 2; i += 4){
                    Bag subBag = new Bag();
                    subBag.colour = tempLine[i] + " " + tempLine[i+1];
                    tempBag.contains.add(subBag);
                }
                mainBags.add(tempBag);
            }
            myReader.close();

            // Fyll inn contains
            for (Bag i : mainBags){
                for (Bag j : mainBags){
                    for (Bag k : j.contains){
                        if (k.colour.equals(i.colour)){
                            i.containedIn.add(j);
                        }
                    }
                }
            }

            /*
            for (Bag i : mainBags) {
                System.out.println("Bag:");
                System.out.println(i.colour);
                System.out.println("Contained in");
                for (Bag j : i.containedIn){
                    System.out.println(j.colour);
                }
            }

             */


            ArrayList<Bag> containsSG = new ArrayList<>();
            // Sjekk om de inneholder shiny gold direkte
            for (Bag i : mainBags){
                for (Bag j : i.contains){
                    if (j.colour.equals("shiny gold")){
                        containsSG.add(i);
                    }
                }
            }

            int sgListLength = containsSG.size();
            int iterator = 0;
            while (iterator < sgListLength){
                ArrayList<Bag> tempSGList = containsSG;
                for (Bag i : containsSG.get(iterator).containedIn){
                    for (Bag j : containsSG){
                        if (!i.colour.equals(j.colour)){
                            tempSGList.add(i);
                            for (Bag k : tempSGList){
                                System.out.println(k.colour);
                            }
                        }
                    }
                }
                containsSG = tempSGList;
                sgListLength = containsSG.size();
                iterator++;
            }

            System.out.println(containsSG.size());



        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }
}

class Bag {
    String colour;
    ArrayList<Bag> contains = new ArrayList<>();
    ArrayList<Bag> containedIn = new ArrayList<>();

    /*
    public ArrayList<Bag> addToContainsSG(ArrayList<Bag> sgList){
        for (Bag i : this.containedIn){
            for (Bag j : sgList){
                if (i.colour.equals(j.colour)){
                    continue;
                } else {
                    sgList.add(i);
                    for (Bag k : sgList){
                        System.out.println(k.colour);
                    }
                }
            }
        }

        return sgList;
    }

     */
}

