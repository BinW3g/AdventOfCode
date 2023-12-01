package Day1;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.InputStream;
import java.util.Scanner;

public class Day1 {

    public static int findCalibrationValue(String text){
        int firstI = 0;
        int lastI = text.length()-1;

        char firstDigit = ' ';
        char lastDigit = ' ';

        while(firstI < text.length()){
            if(firstDigit == ' ' && Character.isDigit(text.charAt(firstI)))
                firstDigit = text.charAt(firstI);
            if(lastDigit == ' ' && Character.isDigit(text.charAt(lastI)))
                lastDigit = text.charAt(lastI);
            if (Character.isDigit(firstDigit) && Character.isDigit(lastDigit))
                break;

            firstI++;
            lastI--;
        }
        return Integer.parseInt(firstDigit + "" + lastDigit);
    }

    public static char checkIfNumber(String number){
        return switch (number) {
            case "zero" -> '0';
            case "one" -> '1';
            case "two" -> '2';
            case "three" -> '3';
            case "four" -> '4';
            case "five" -> '5';
            case "six" -> '6';
            case "seven" -> '7';
            case "eight" -> '8';
            case "nine" -> '9';
            default -> ' ';
        };
    }
    public static int findCorrectCalibrationValue(String text){
        int firstI = 0;
        int lastI = text.length()-1;

        char firstDigit = ' ';
        char lastDigit = ' ';

        while(firstI < text.length()){
            if (firstDigit == ' ' && Character.isDigit(text.charAt(firstI)))
                firstDigit = text.charAt(firstI);
            else {
                if (firstDigit == ' ' && firstI + 3 < text.length())
                    firstDigit = checkIfNumber(text.substring(firstI, firstI + 3));
                if (firstDigit == ' ' && firstI + 4 < text.length())
                    firstDigit = checkIfNumber(text.substring(firstI, firstI + 4));
                if (firstDigit == ' ' && firstI + 5 < text.length())
                    firstDigit = checkIfNumber(text.substring(firstI, firstI + 5));
            }
            if (lastDigit == ' ' && Character.isDigit(text.charAt(lastI))) {
                lastDigit = text.charAt(lastI);
            } else {
                if (lastDigit == ' ' && lastI - 4 > 0)
                    lastDigit = checkIfNumber(text.substring(lastI - 4, lastI+1));
                if (lastDigit == ' ' && lastI - 3 > 0)
                    lastDigit = checkIfNumber(text.substring(lastI - 3, lastI+1));
                if (lastDigit == ' ' && lastI - 2 > 0)
                    lastDigit = checkIfNumber(text.substring(lastI - 2, lastI+1));
            }

            if (Character.isDigit(firstDigit) && Character.isDigit(lastDigit))
                break;

            firstI++;
            lastI--;
        }
        return Integer.parseInt(firstDigit + "" + lastDigit);
    }

    public InputStream getFile(){
        return this.getClass().getResourceAsStream("input.txt");
    }

    public static void main(String[] args) {
        int wrongSum = 0;
        int correctSum = 0;
        Day1 d = new Day1();
        Scanner fileReader = new Scanner(d.getFile());
        while(fileReader.hasNextLine()){
            String line = fileReader.nextLine();
//            wrongSum += findCalibrationValue(line);
            correctSum += findCorrectCalibrationValue(line);
        }
        System.out.println("part 1: " + wrongSum);
        System.out.println("part 2: " + correctSum);
    }
}
