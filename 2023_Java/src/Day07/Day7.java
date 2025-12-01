package Day07;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Day7 {

    public int part1_totalWinnings() {
        Scanner input = new Scanner(getClass().getResourceAsStream("input.txt"));
        List<PokerHands> hands = new ArrayList<>();
        while (input.hasNext()) {
            String line = input.nextLine();
            String[] tokens = line.split(" "); //0 hand, 1 bid
            hands.add(new PokerHands(tokens[0], tokens[1]));
        }
        hands.sort(PokerHands::compareTo);
        int rank = 1;
        int sumOfWinnings = 0;
        for (PokerHands hand : hands) {
            sumOfWinnings += hand.bid * rank;
            rank++;
        }

        return sumOfWinnings;
    }

    public int part2_totalWinningsWithJokers() {
        Scanner input = new Scanner(getClass().getResourceAsStream("input.txt"));
        List<PokerHandsWithJokers> hands = new ArrayList<>();
        while (input.hasNext()) {
            String line = input.nextLine();
            String[] tokens = line.split(" "); //0 hand, 1 bid
            hands.add(new PokerHandsWithJokers(tokens[0], tokens[1]));
        }
        hands.sort(PokerHandsWithJokers::compareTo);
        int rank = 1;
        int sumOfWinnings = 0;
        for (PokerHandsWithJokers hand : hands) {
            sumOfWinnings += hand.bid * rank;
            rank++;
        }

        return sumOfWinnings;
    }

    public static void main(String[] args) {
        Day7 d7 = new Day7();
        System.out.println(d7.part1_totalWinnings());
        System.out.println(d7.part2_totalWinningsWithJokers());
    }
}
