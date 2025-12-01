package Day09;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Day9 {

    public boolean isAllZero(List<Integer> toCheck){
        for(int num : toCheck){
            if(num != 0){
                return false;
            }
        }
        return true;
    }

    public int[] part1_and_part2_sumOfExtrapolatedValues(){
        Scanner scan = new Scanner(getClass().getResourceAsStream("input.txt"));
        int[] extrapolatedSum = new int[2];
        while(scan.hasNext()) {
            String line = scan.nextLine();
            List<List<Integer>> readings = new ArrayList<>();
            readings.add(new ArrayList<>());
            for(String number : line.split(" ")){
                readings.get(0).add(Integer.valueOf(number));
            }
            do{
                List<Integer> oldReadings = readings.get(readings.size() - 1);
                List<Integer> newReadings = new ArrayList<>();
                for (int i = 0; i < oldReadings.size()-1; i++) {
                    newReadings.add(oldReadings.get(i+1) - oldReadings.get(i));
                }
                readings.add(newReadings);
            }while (!isAllZero(readings.get(readings.size()-1)));
            for (int i = readings.size()-1; i >0; i--) {
                List<Integer> current = readings.get(i);
                List<Integer> next = readings.get(i-1);
                next.add(current.get(current.size()-1)+ next.get(next.size()-1));
                next.add(0, next.get(0) - current.get(0));
            }
           extrapolatedSum[1] += readings.get(0).get(readings.get(0).size()-1);
           extrapolatedSum[0] += readings.get(0).get(0);
        }
        return extrapolatedSum;
    }


    public static void main(String[] args) {
        Day9 d9 = new Day9();
        int[] solution = d9.part1_and_part2_sumOfExtrapolatedValues();
        System.out.println("Part1: " + solution[1]);
        System.out.println("Part2: " + solution[0]);
    }
}
