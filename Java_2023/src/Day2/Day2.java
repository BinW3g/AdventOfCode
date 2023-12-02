package Day2;

import java.util.Scanner;

public class Day2 {
    public int part1() {
        final int MAX_RED_CUBES = 12;
        final int MAX_GREEN_CUBES = 13;
        final int MAX_BLUE_CUBES = 14;

        Scanner scan = new Scanner(this.getClass().getResourceAsStream("input.txt"));

        int gameIdSum = 0;
        while (scan.hasNextLine()) {
            String line = scan.nextLine();
            String[] tokens = line.split(": ");
            int gameID = Integer.parseInt(tokens[0].split(" ")[1]);
            String[] sets = tokens[1].split("; ");
            String[] reveals;
            boolean validSet = true;

            gameCheck:
            for (String set : sets) {
                reveals = set.split(", ");
                for (String reveal : reveals) {
                    tokens = reveal.split(" ");
                    int cubeNumber = Integer.parseInt(tokens[0]);
                    validSet = switch (tokens[1]) {
                        case "blue" -> cubeNumber <= MAX_BLUE_CUBES;
                        case "red" -> cubeNumber <= MAX_RED_CUBES;
                        case "green" -> cubeNumber <= MAX_GREEN_CUBES;
                        default -> validSet;
                    };
                    if (!validSet) break gameCheck;
                }
            }
            if (validSet)
                gameIdSum += gameID;
        }

        return gameIdSum;
    }

    public int part2() {
        Scanner scan = new Scanner(this.getClass().getResourceAsStream("input.txt"));

        int powerSum = 0;
        while (scan.hasNextLine()) {
            String line = scan.nextLine();
            String[] tokens = line.split(": ");
            String[] sets = tokens[1].split("; ");
            String[] reveals;

            int[] maxColor = {0, 0, 0};
            for (String set : sets) {
                reveals = set.split(", ");
                for (String reveal : reveals) {
                    tokens = reveal.split(" ");
                    int cubeNumber = Integer.parseInt(tokens[0]);
                    switch (tokens[1]) {
                        case "blue":
                            if (cubeNumber > maxColor[0]) maxColor[0] = cubeNumber;
                            break;
                        case "red":
                            if (cubeNumber > maxColor[1]) maxColor[1] = cubeNumber;
                            break;
                        case "green":
                            if (cubeNumber > maxColor[2]) maxColor[2] = cubeNumber;
                            break;
                    }
                }
            }
            powerSum += maxColor[0] * maxColor[1] * maxColor[2];
        }

        return powerSum;
    }


    public static void main(String[] args) {
        Day2 d2 = new Day2();
        System.out.println(d2.part1());
        System.out.println(d2.part2());
    }


}
