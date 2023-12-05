package Day5;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Day5 {
    public long part1_findLowestLocation(){
        Scanner input = new Scanner(getClass().getResourceAsStream("input.txt"));
        String firstLine = input.nextLine();
        long[] seeds = Arrays.stream(firstLine.split(": ")[1].split(" ")).mapToLong(Long::parseLong).toArray();
        boolean[] hasChanged = new boolean[seeds.length];

        while(input.hasNextLine()){
            String line = input.nextLine();
            if(line.isEmpty()){
                hasChanged = new boolean[seeds.length];
                continue;
            }
            if(line.contains(":")){
                continue;
            }

            String[] tokens = line.split(" ");
            long sourceStart = Long.parseLong(tokens[1]);
            long destStart = Long.parseLong(tokens[0]);
            long range = Long.parseLong(tokens[2]);

            for (int i = 0; i < seeds.length; i++) {
                if(hasChanged[i]){
                    continue;
                }
                if(seeds[i] >= sourceStart && seeds[i] < sourceStart+range){
                    long dif = Math.abs(sourceStart - seeds[i]);
                    seeds[i] = destStart + dif;
                    hasChanged[i] = true;
                }
            }
        }
        return Arrays.stream(seeds).min().getAsLong();
    }

    public long part2_findLowestLocationSeedRangesStupidEdition(){
        Scanner input = new Scanner(getClass().getResourceAsStream("input.txt"));
        String firstLine = input.nextLine();
        long[] seeds = Arrays.stream(firstLine.split(": ")[1].split(" ")).mapToLong(Long::parseLong).toArray();
        List<Long> seedsList = new ArrayList<>();
        long counter =0;
        for (int i = 0; i < seeds.length; i+=2) {
            for (int j = 0; j < seeds[i+1]; j++) {
                seedsList.add(seeds[i]+j);
                counter ++;
                if(counter%100000 == 0){
                    System.out.println(seedsList.size());
                }
            }
        }
        boolean[] hasChanged = new boolean[seedsList.size()];
        while(input.hasNextLine()){
            String line = input.nextLine();
            if(line.isEmpty()){
                hasChanged = new boolean[seedsList.size()];
                continue;
            }
            if(line.contains(":")){
                continue;
            }

            String[] tokens = line.split(" ");
            long sourceStart = Long.parseLong(tokens[1]);
            long destStart = Long.parseLong(tokens[0]);
            long range = Long.parseLong(tokens[2]);

            int i = -1;
            for (long seed : seedsList) {
                i++;
                if(hasChanged[i]){
                    continue;
                }
                if(seed >= sourceStart && seed < sourceStart+range){
                    long dif = Math.abs(sourceStart - seed);
                    seedsList.set(i, destStart + dif);
                    hasChanged[i] = true;
                }
            }
        }
        return seedsList.stream().mapToLong(v -> v).min().orElseThrow();
    }

    public long part2_findLowestLocationSeedRanges(){
        Scanner input = new Scanner(getClass().getResourceAsStream("input.txt"));
        String firstLine = input.nextLine();
        String[] stringSeeds = firstLine.split(": ")[1].split(" ");
        List<SeedRange> seeds = new ArrayList<>();
        for (int i = 0; i < stringSeeds.length; i+=2) {
            seeds.add(new SeedRange(stringSeeds[i], stringSeeds[i+1]));
        }

        while(input.hasNextLine()) {
            String line = input.nextLine();
            if (line.isEmpty()) {
                for (SeedRange seed : seeds) {
                    seed.setAllowChange(true);
                }
                continue;
            }
            if (line.contains(":")) {
                continue;
            }

            String[] tokens = line.split(" ");
            long sourceStart = Long.parseLong(tokens[1]);
            long destStart = Long.parseLong(tokens[0]);
            long range = Long.parseLong(tokens[2]);
            for (int i = 0; i < seeds.size(); i++) {
                SeedRange seed = seeds.get(i);
                if (!seed.isAllowChange()) {
                    continue;
                }
                if(sourceStart > seed.getSeed()  &&  sourceStart <= seed.getSeed()+seed.getRange()){
                    seeds.add(seed.splitSeedAt(sourceStart));
                }

                if (seed.getSeed() >= sourceStart && seed.getSeed() < sourceStart + range) {
                    if (seed.getRange() > range) {
                        seeds.add(seed.outOfRange(range));
                    }
                    long dif = Math.abs(sourceStart - seed.getSeed());
                    seed.setSeed(destStart + dif);
                    seed.setAllowChange(false);
                }
            }
        }

        long min = Long.MAX_VALUE;
        for (SeedRange seed : seeds) {
            if (min > seed.getSeed()){
                min = seed.getSeed();
            }
        }
        return min;
    }

    public static void main(String[] args) {
        Day5 d5 = new Day5();
        long startTime = System.currentTimeMillis();
        System.out.println(d5.part1_findLowestLocation());
        System.out.println((System.currentTimeMillis() - startTime) + "ms");
        System.out.println(d5.part2_findLowestLocationSeedRanges());
        System.out.println((System.currentTimeMillis() - startTime) + "ms");
    }
}
