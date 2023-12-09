package Day06;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Day6 {
    public int part1_calcWinningTimes() {
        Scanner input = new Scanner(getClass().getResourceAsStream("input.txt"));
        String line = input.nextLine();
        String[] tokens = line.split(":")[1].split(" ");
        List<RaceInfos> raceInfos = new ArrayList<>();

        for (String token :
                tokens) {
            if (token.isEmpty()) continue;
            raceInfos.add(new RaceInfos(Integer.parseInt(token)));
        }

        line = input.nextLine();
        tokens = line.split(":")[1].split(" ");
        int currentRace = 0;
        for (String token : tokens) {
            if (token.isEmpty()) continue;
            raceInfos.get(currentRace).distanceToWin = Integer.parseInt(token);
            currentRace++;
        }

        int sumOfWinnings = 1;
        int winCounter = 0;
        for (RaceInfos race : raceInfos) {
            for (int i = 0; i < race.timeOfRace; i++) {
                if (i * (race.timeOfRace - i) > race.distanceToWin) {
                    winCounter++;
                }
            }
            sumOfWinnings *= winCounter;
            winCounter = 0;
        }

        return sumOfWinnings;
    }

    public int part2_RaceInfoInterpretedDiffrently() {
        Scanner input = new Scanner(getClass().getResourceAsStream("input.txt"));
        String line = input.nextLine();
        String[] tokens = line.split(":")[1].split(" ");


        String raceTimeNumber = "";
        for (String token : tokens) {
            raceTimeNumber += token;
        }

        line = input.nextLine();
        tokens = line.split(":")[1].split(" ");
        String distanceToWinString = "";
        for (String token : tokens) {
            distanceToWinString += token;
        }

        Long raceTime = Long.parseLong(raceTimeNumber);
        Long distanceToWin = Long.parseLong(distanceToWinString);

        int winCounter = 0;
        for (int i = 0; i < raceTime; i++) {
            if (i * (raceTime - i) > distanceToWin) {
                winCounter++;
            }
        }
        return winCounter;
    }

    public static void main(String[] args) {
        Day6 d6 = new Day6();
        System.out.println(d6.part1_calcWinningTimes());
        System.out.println(d6.part2_RaceInfoInterpretedDiffrently());
    }
}
