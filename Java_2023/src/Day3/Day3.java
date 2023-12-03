package Day3;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Stream;

public class Day3 {
    public List<List<Object>> readInput() {
        Scanner scan = new Scanner(this.getClass().getResourceAsStream("input.txt"));
        List<List<Object>> inputArray = new ArrayList<>();

        int currentLine = 0;
        while (scan.hasNextLine()) {
            String line = scan.nextLine();
            inputArray.add(new ArrayList<>());

            char[] charArray = line.toCharArray();
            for (int i = 0; i < charArray.length; i++) {
                char c = charArray[i];
                if (!Character.isDigit(c)) {
                    inputArray.get(currentLine).add(c);
                    continue;
                }

                int j = i;
                //find the entire number
                String numberString = "";
                while (j < charArray.length && Character.isDigit(charArray[j])) {
                    numberString += charArray[j];
                    j++;
                }
                //Add the hole number to every field
                MyInteger foundNumber = new MyInteger(Integer.parseInt(numberString));
                for (int k = i; k < j; k++) {
                    inputArray.get(currentLine).add(foundNumber);
                }
                i = j - 1;

            }
            currentLine++;
        }
        return inputArray;
    }

    private static List<Integer> getAdjacentNumbers(int currentLine, int currentColumn, List<List<Object>> input) {
        List<Integer> adjacentNumber = new ArrayList<>();
        for (int i = currentLine - 1; i <= currentLine + 1; i++) {
            for (int j = currentColumn - 1; j <= currentColumn + 1; j++) {
                if (i < 0 || i >= input.get(currentLine).size() || j < 0 || j >= input.size())
                    continue;
                Object current = input.get(i).get(j);
                if(current instanceof MyInteger && ((MyInteger) current).getIntegerValue() != 0){
                    adjacentNumber.add(((MyInteger) current).getIntegerValue());
                    ((MyInteger) current).setIntegerValue(0);
                }
            }
        }
        return adjacentNumber;
    }

    public int part1_SumOfPartNumbers() {
        int partSum = 0;
        List<List<Object>> input = readInput();

        int currentLine = 0;
        for (List<Object> line : input) {
            int currentColumn = -1;
            for(Object o:line){
                currentColumn++;
                if (!(o instanceof Character)) {
                    continue;
                }
                if ((char) o == '.') {
                    continue;
                }
                partSum += getAdjacentNumbers(currentLine, currentColumn, input).stream().mapToInt(Integer::valueOf).sum();
            }
            currentLine++;
        }
        return partSum;
    }

    public int part2_SumOfGearRatios() {
        int gearRatio = 0;
        List<List<Object>> input = readInput();

        int currentLine = 0;
        for (List<Object> line : input) {
            int currentColumn = -1;
            for(Object o:line){
                currentColumn++;
                if (!(o instanceof Character))
                    continue;
                if ((char) o != '*')
                    continue;

                List<Integer> adjacent = getAdjacentNumbers(currentLine, currentColumn, input);
                if(adjacent.size() == 2){
                    gearRatio+= adjacent.get(0) * adjacent.get(1);
                }
            }
            currentLine++;
        }
        return gearRatio;
    }


    public static void main(String[] args) {
        Day3 d3 = new Day3();
        System.out.println(d3.part1_SumOfPartNumbers());
        System.out.println(d3.part2_SumOfGearRatios());
    }
}
