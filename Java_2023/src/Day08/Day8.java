package Day08;

import java.util.*;

public class Day8 {
    private Map<String, String[]> graph = new HashMap<>();
    private String instructions = "";
    public void init() {
        Scanner scan = new Scanner(getClass().getResourceAsStream("input.txt"));
        instructions = scan.nextLine();
        scan.nextLine();
        while(scan.hasNextLine()){
            String line = scan.nextLine();
            String[] tokens = line.split(" = ");
            String note = tokens[0];
            tokens = tokens[1].split(", ");
            graph.put(note, new String[]{tokens[0].substring(1), tokens[1].substring(0, tokens[1].length()-1)});
        }
    }

    public long part1_findSteps(String startNode){
        long steps = 0;
        if(graph.isEmpty()) return -1;
        if(instructions.isEmpty()) return -1;

        String currentNode = startNode;
        int instructionIndex = 0;
        while(!currentNode.endsWith("Z")){
            if(instructionIndex == instructions.length()){
                instructionIndex=0;
            }
            String[] paths = graph.get(currentNode);
            currentNode = switch (instructions.charAt(instructionIndex)) {
                case 'L' -> paths[0];
                case 'R' -> paths[1];
                default -> throw new UnsupportedOperationException();
            };
            steps ++;
            instructionIndex++;
        }
        return steps;
    }

    public static long lcm(long number1, long number2) {
        if (number1 == 0 || number2 == 0) {
            return 0;
        }

        long absHigherNumber = Math.max(number1, number2);
        long absLowerNumber = Math.min(number1, number2);
        long lcm = absHigherNumber;
        while (lcm % absLowerNumber != 0) {
            lcm += absHigherNumber;
        }
        return lcm;
    }

    public long part2_findStepsMultiple(){
        long totalSteps = -1;
        if(graph.isEmpty()) return -1;
        if(instructions.isEmpty()) return -1;

        List<Long> steps = new ArrayList<>();
        for (String node:graph.keySet()) {
            if(node.endsWith("A")){
               steps.add(part1_findSteps(node));
            }
        }

        for(long step : steps){
            totalSteps = lcm(totalSteps, step);
        }


        return totalSteps;
    }

//    public long part2_findStepsMultipleBruteForce(){
//        long steps = 0;
//        if(graph.isEmpty()) return -1;
//        if(instructions.isEmpty()) return -1;
//
//        List<String> currentNodes = new ArrayList<>();
//        for (String node:graph.keySet()) {
//            if(node.endsWith("A")){
//                currentNodes.add(node);
//            }
//        }
//
//
//        int instructionIndex = 0;
//        while(!allEndInZ(currentNodes)){
//            if(instructionIndex == instructions.length()){
//                instructionIndex=0;
//            }
//            int i =0;
//            for(String currentNode:currentNodes){
//                String[] paths = graph.get(currentNode);
//                currentNode = switch (instructions.charAt(instructionIndex)) {
//                    case 'L' -> paths[0];
//                    case 'R' -> paths[1];
//                    default -> throw new UnsupportedOperationException();
//                };
//                currentNodes.set(i, currentNode);
//                i++;
//            }
//            steps ++;
//            instructionIndex++;
//        }
//        return steps;
//    }

    public static void main(String[] args) {
        Day8 d8 = new Day8();
        d8.init();
        System.out.println(d8.part1_findSteps("AAA"));
        System.out.println(d8.part2_findStepsMultiple());
    }




}
