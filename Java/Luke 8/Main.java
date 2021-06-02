import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.List;
import java.util.Scanner; // Import the Scanner class to read text files
import java.util.ArrayList;


public class Main {
    public static void main(String[] args) {

        ArrayList<Instruction> instructionList = new ArrayList<>();

        try {
            // Hent info
            File myObj = new File("input.txt");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String input = myReader.nextLine();
                String[] tempLine = input.split(" ");

                Instruction tempIns = new Instruction();
                tempIns.instruction = tempLine[0];
                tempIns.step = Integer.parseInt(tempLine[1]);
                tempIns.posistion = instructionList.size();

                instructionList.add(tempIns);
            }
            myReader.close();

            // Kjører gjennom

            ArrayList<Instruction> list = new ArrayList<>();
            for (Instruction i : instructionList){
                list.add(i);
            }

            boolean completed = false;
            int accum = 0;

            int instructionNr = -1;
            while (!completed && instructionNr < list.size()-1){
                int line = 0;
                accum = 0;
                completed = true;

                instructionNr++;
                switch (list.get(instructionNr).instruction){
                    case "nop" -> list.get(instructionNr).instruction = "jmp";
                    case "jmp" -> list.get(instructionNr).instruction = "nop";
                }

                while (line < list.size()){
                    if (list.get(line).executed) {
                        completed = false;
                        switch (list.get(instructionNr).instruction){
                            case "nop" -> list.get(instructionNr).instruction = "jmp";
                            case "jmp" -> list.get(instructionNr).instruction = "nop";
                        }
                        break;
                    } else {
                        list.get(line).executed = true;
                        list.get(line).accumulated = accum;
                        int saveLine = line;

                        switch (list.get(line).instruction) {
                            case "nop" -> line++;
                            case "acc" -> {
                                accum += list.get(line).step;
                                line++;
                            }
                            case "jmp" -> line += list.get(line).step;
                        }
                        if (line < list.size()){
                            list.get(line).previousLinePos = saveLine;
                        }
                    }
                }
            }



            System.out.println(accum);

        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }


}

class Instruction {
    String instruction;
    int step;
    int previousLinePos;
    boolean executed = false;
    int posistion;
    int accumulated;
}
/*
class MethodClass {
    public int runCode(ArrayList<Instruction> list, int accum, int startPos){
        int line = startPos;
        boolean somethingChanged = false;
        int changedLine = 0;
        int previousLine;

        while (line < list.size()){
            System.out.println("---------------------");
            System.out.println(line);
            if (list.get(line).executed) {
                // Del 2:

                previousLine = list.get(line).previousLinePos;
                if (somethingChanged){
                    somethingChanged = false;
                    switch (list.get(changedLine).instruction) {
                        case "nop" -> {
                            list.get(changedLine).instruction = "jmp";
                            line = list.get(changedLine).previousLinePos;
                        }
                        case "acc" -> {

                            line = list.get(changedLine).previousLinePos;
                        }
                        case "jmp" -> {
                            list.get(changedLine).instruction = "nop";
                            line = list.get(changedLine).previousLinePos;
                        }
                    }
                    accum = list.get(list.get(changedLine).previousLinePos).accumulated;
                } else {
                    switch (list.get(previousLine).instruction) {
                        case "nop" -> {
                            list.get(previousLine).instruction = "jmp";
                            list.get(previousLine).executed = false;
                            changedLine = previousLine;
                            line = previousLine;
                            somethingChanged = true;
                        }
                        case "acc" -> {
                            accum -= list.get(previousLine).step;
                            line = list.get(previousLine).previousLinePos;
                            list.get(line).executed = false;
                            while (list.get(line).instruction.equals("acc")){
                                accum -= list.get(line).step;
                                line = list.get(line).previousLinePos;
                                list.get(line).executed = false;
                            }
                        }
                        case "jmp" -> {
                            list.get(previousLine).instruction = "nop";
                            list.get(previousLine).executed = false;
                            changedLine = previousLine;
                            line = previousLine;
                            somethingChanged = true;
                        }
                    }
                }

                // Del 1: break;
            } else {
                list.get(line).executed = true;
                list.get(line).accumulated = accum;
                int saveLine = line;

                System.out.println(list.get(line).instruction);
                switch (list.get(line).instruction) {
                    case "nop" -> line++;
                    case "acc" -> {
                        accum += list.get(line).step;
                        line++;
                    }
                    case "jmp" -> line += list.get(line).step;
                }
                if (line < list.size()){
                    list.get(line).previousLinePos = saveLine;
                }
            }
        }

        return accum;
    }
}
*/

            /*
            // Printer ut lista
            for (Instruction i : instructionList){
                System.out.println(i.instruction + " " + String.valueOf(i.step) + " " + String.valueOf(i.posistion));
            }
            */

            /*
            boolean changeNeeded = false;
            boolean passable = true;


            // Fikser lista
            for (Instruction i : instructionList){
                if (i.instruction.equals("jmp") && i.step < 0){
                    int passingElementPos = 0;
                    for (int j = i.posistion - 1; j > - 1; j--){
                        if (instructionList.get(j).step + instructionList.get(j).posistion >= i.posistion){
                            if (instructionList.get(j).instruction.equals("jmp")){
                                passingElementPos = j;
                                changeNeeded = false;
                                break;
                            } else if (instructionList.get(j).instruction.equals("nop")){
                                passingElementPos = j;
                                passable = true;
                                changeNeeded = true;
                            }
                        } else {
                            changeNeeded = true;
                            passable = false;
                        }
                    }

                    System.out.println("--------------------");
                    System.out.println("Passable: " + passable);
                    System.out.println("Change needed: " + changeNeeded);

                    if (changeNeeded && passable){
                        System.out.println("Changed nop to jmp");
                        instructionList.get(passingElementPos).instruction = "jmp";
                    } else if (changeNeeded){
                        i.instruction = "nop";
                        System.out.println("Changed jmp to nop");
                    }

                }
            }
            */


/*
class ListComplete {
    boolean completed = false;
    int sum = 0;
}
 */


/*
public static ListComplete runCode(ArrayList<Instruction> list, int accum, int startPos){
        ListComplete result = new ListComplete();
        result.sum = accum;
        int line = startPos;
        while (line < list.size() - 1){
            if (list.get(line).executed) {
                // Del 2:
                switch (list.get(list.get(line).previousLinePos).instruction) {
                    case "nop" -> {
                        list.get(list.get(line).previousLinePos).instruction = "jmp";
                        result = runCode(list, result.sum, list.get(line).previousLinePos);
                        if (result.completed){
                            return result;
                        } else {
                            list.get(list.get(line).previousLinePos).instruction = "nop";
                            result = runCode(list, result.sum, list.get(list.get(line).previousLinePos).previousLinePos);
                        }

                    }
                    case "acc" -> {

                        accum += list.get(line).step;
                        line++;
                    }
                    case "jmp" -> line += list.get(line).step;
                }


                // Del 1: break;
            } else {
                    list.get(line).executed = true;
                    list.get(line).previousLinePos = line;
                    switch (list.get(line).instruction) {
                    case "nop" -> line++;
                    case "acc" -> {
                    result.sum += list.get(line).step;
                    line++;
                    }
                    case "jmp" -> line += list.get(line).step;
                    }
                    }
                    }

                    result.completed = true;
                    return result;
                    }
 */