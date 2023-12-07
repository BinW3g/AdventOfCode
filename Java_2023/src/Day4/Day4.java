package Day4;

import java.util.*;

public class Day4 {

    public int part1_sumOfWinnings() {
        int sum = 0;

        Scanner cards = new Scanner(this.getClass().getResourceAsStream("input.txt"));
        while (cards.hasNextLine()) {
            String card = cards.nextLine();
            String[] tokens = card.split(": ")[1].split(" \\| ");
            int[] winningNumbers = Arrays.stream(tokens[0].split(" ")).mapToInt(x -> (x.isEmpty()) ? -1 : Integer.parseInt(x)).toArray();
            int[] myNumbers = Arrays.stream(tokens[1].split(" ")).mapToInt(x -> (x.isEmpty()) ? -1 : Integer.parseInt(x)).toArray();

            int matchCount = 0;
            for (int winningNr : winningNumbers) {
                if (winningNr != -1 && Arrays.stream(myNumbers).anyMatch(value -> value == winningNr)) {
                    matchCount++;
                }
            }
            sum += (matchCount > 0) ? (int) Math.pow(2, matchCount - 1) : 0;
        }

        return sum;
    }

    public int part2_sumOfTotalScratchcardsNewRules() {
        int scratchcardTotal = 0;
        int duplicationCounter = 0;
        List<Integer> nextCopies = new ArrayList<>();
        List<Integer> instances = new ArrayList<>();

        Scanner cards = new Scanner(this.getClass().getResourceAsStream("input.txt"));
        while (cards.hasNextLine()) {
            String card = cards.nextLine();
            String[] tokens = card.split(": ")[1].split(" \\| ");
            int[] winningNumbers = Arrays.stream(tokens[0].split(" ")).mapToInt(x -> (x.isEmpty()) ? -1 : Integer.parseInt(x)).toArray();
            int[] myNumbers = Arrays.stream(tokens[1].split(" ")).mapToInt(x -> (x.isEmpty()) ? -1 : Integer.parseInt(x)).toArray();

            int winnings = 0;
            for (int winningNr : winningNumbers) {
                if (winningNr != -1 && Arrays.stream(myNumbers).anyMatch(value -> value == winningNr)) {
                    winnings++;
                }
            }
            int currentCard = 1;
            if (!nextCopies.isEmpty())
                currentCard = nextCopies.remove(0);
            for (int i = 0; i < winnings; i++) {
                if (i >= nextCopies.size()) {
                    nextCopies.add(1 + currentCard);
                } else {
                    nextCopies.set(i, nextCopies.get(i) + currentCard);
                }
            }
            scratchcardTotal += currentCard;
            instances.add(currentCard);

        }

        return scratchcardTotal;
    }


    public static void main(String[] args) {
        Day4 d4 = new Day4();
        System.out.println(d4.part1_sumOfWinnings());
        System.out.println(d4.part2_sumOfTotalScratchcardsNewRules());
    }
}
