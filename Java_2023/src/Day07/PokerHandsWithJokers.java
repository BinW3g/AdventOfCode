package Day07;

import Day03.MyInteger;

import java.util.*;

public class PokerHandsWithJokers implements Comparable<PokerHandsWithJokers> {
    protected String hand;
    protected int bid;

    private final int strength;


    public PokerHandsWithJokers(String hand, String bid) {
        this.hand = hand;
        this.bid = Integer.parseInt(bid);
        this.strength = findStrengthOfHand();
    }

    public String getHand() {
        return hand;
    }

    public void setHand(String hand) {
        this.hand = hand;
    }

    public int getBid() {
        return bid;
    }

    public void setBid(int bid) {
        this.bid = bid;
    }

    @Override
    public String toString() {
        return "PokerHands{" +
                "hand='" + hand + '\'' +
                ", bid=" + bid +
                ", strength=" + strength +
                '}';
    }

    private int findStrengthOfHand() {
        Map<Character, MyInteger> amount = new HashMap<>();
        int countJokers = 0;
        for (char c : hand.toCharArray()) {
            if (c == 'J') {
                countJokers++;
                continue;
            }
            if (amount.containsKey(c)) {
                amount.get(c).incrementValue(1);
            } else {
                amount.put(c, new MyInteger(1));
            }
        }

        Set<Character> keys = amount.keySet();
        if (keys.size() == 1 || countJokers == 5) {
            return 6; //five of a kind
        }

        for (int i = 0; i < countJokers; i++) {
            char key = amount.entrySet().stream().max(Comparator.comparingInt(entry -> entry.getValue().getIntegerValue())).get().getKey();
            amount.get(key).incrementValue(1);
        }

        int count3 = 0;
        int count2 = 0;
        int count1 = 0;
        for (char key : keys) {
            switch (amount.get(key).getIntegerValue()) {
                case 4:
                    return 5; //Four of a kind
                case 3:
                    count3++;
                    break;
                case 2:
                    count2++;
                    break;
                case 1:
                    count1++;
            }
        }
        if (count3 == 1 && count2 == 1) {
            return 4; //full house
        }
        if (count3 == 1) {
            return 3; //three of a kind
        }
        if (count2 == 2) {
            return 2;//two pair
        }
        if (count2 == 1) {
            return 1; //one pair
        }
        if (count1 == 5) {
            return 0;
        }
        return -1;
    }

    private int getValueOfSymbol(char c) {
        if (Character.isDigit(c)) {
            return Integer.parseInt(c + "");
        }
        return switch (c) {
            case 'T' -> 10;
            case 'J' -> 1;
            case 'Q' -> 12;
            case 'K' -> 13;
            case 'A' -> 14;
            default -> -1;
        };

    }

    @Override
    public int compareTo(PokerHandsWithJokers o) {
        if (o.strength != this.strength) {
            return this.strength - o.strength;
        }

        for (int i = 0; i < hand.length(); i++) {
            if (o.hand.charAt(i) != this.hand.charAt(i)) {
                return getValueOfSymbol(this.hand.charAt(i)) - getValueOfSymbol(o.hand.charAt(i));
            }
        }
        return 0;
    }
}
