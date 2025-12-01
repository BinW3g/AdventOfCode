package Day10;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class Day10 {

    public char[][] mapInput() {
        Scanner scan = new Scanner(getClass().getResourceAsStream("input.txt"));
        List<char[]> lines = new LinkedList<>();
        while (scan.hasNext()) {
            lines.add(scan.next().toCharArray());
        }
        char[][] map = new char[lines.size()][];
        int i = 0;
        for (char[] line : lines) {
            map[i] = line;
            i++;
        }
        return map;
    }

    public int part1_findFurthestFromStart() {
        char[][] map = mapInput();

        //find start
        int currentX = -1;
        int currentY = -1;
        outer:
        for (int i = 0; i < map.length; i++) {
            for (int j = 0; j < map[i].length; j++) {
                if (map[i][j] == 'S') {
                    currentX = j;
                    currentY = i;
                    break outer;
                }
            }
        }

        int pathLength = 1;
        currentY++;
        int verticalStep = 1;
        int horizontalStep = 0;
        while (map[currentY][currentX] != 'S') {
            switch (map[currentY][currentX]) {
                case '|':
                case '-':
                    break;
                case 'L':
                    if (verticalStep == 1) {
                        verticalStep = 0;
                        horizontalStep = 1;
                    } else if (horizontalStep == -1) {
                        verticalStep = -1;
                        horizontalStep = 0;
                    }
                    break;
                case 'J':
                    if (verticalStep == 1) {
                        verticalStep = 0;
                        horizontalStep = -1;
                    } else if (horizontalStep == 1) {
                        verticalStep = -1;
                        horizontalStep = 0;
                    }
                    break;
                case '7':
                    if (verticalStep == -1) {
                        verticalStep = 0;
                        horizontalStep = -1;
                    } else if (horizontalStep == 1) {
                        verticalStep = 1;
                        horizontalStep = 0;
                    }
                    break;
                case 'F':
                    if (verticalStep == -1) {
                        verticalStep = 0;
                        horizontalStep = 1;
                    } else if (horizontalStep == -1) {
                        verticalStep = 1;
                        horizontalStep = 0;

                    }
                    break;
                default:
                    System.out.println(map[currentY][currentX]);
                    throw new RuntimeException();

            }
            pathLength++;
            currentX += horizontalStep;
            currentY += verticalStep;
        }
        return pathLength / 2;
    }

    public int part2_findEnclosed() {
        char[][] small_map = mapInput();
        //blow up input
        char[][] map = new char[small_map.length][];
        for (int i = 0; i < map.length; i++) {
            map[i] = new char[small_map[i].length*2];
            for (int j = 0; j < map[i].length-1; j+=2) {
                map[i][j] = small_map[i][j/2];
                if(map[i][j] == 'F' || map[i][j] == '-' || map[i][j] == 'L'){
                    map[i][j+1] = '-';
                }else {
                    map[i][j+1] = '.';
                }
            }
        }
        printArray(map);
        //find start
        int currentX = -1;
        int currentY = -1;
        outer:
        for (int i = 0; i < map.length; i++) {
            for (int j = 0; j < map[i].length; j++) {
                if (map[i][j] == 'S') {
                    currentX = j;
                    currentY = i;
                    break outer;
                }
            }
        }

        currentY++;
        int verticalStep = 1;
        int horizontalStep = 0;
        while (map[currentY][currentX] != 'S') {
            switch (map[currentY][currentX]) {
                case '|':
                    map[currentY][currentX] = 's';
                    break;
                case '-':
                    map[currentY][currentX] = 'p';
                    break;
                case 'L':
                    if (verticalStep == 1) {
                        verticalStep = 0;
                        horizontalStep = 1;
                    } else if (horizontalStep == -1) {
                        verticalStep = -1;
                        horizontalStep = 0;
                    }
                    map[currentY][currentX] = 'o';
                    break;
                case 'J':
                    if (verticalStep == 1) {
                        verticalStep = 0;
                        horizontalStep = -1;
                    } else if (horizontalStep == 1) {
                        verticalStep = -1;
                        horizontalStep = 0;
                    }
                    map[currentY][currentX] = 'c';
                    break;
                case '7':
                    if (verticalStep == -1) {
                        verticalStep = 0;
                        horizontalStep = -1;
                    } else if (horizontalStep == 1) {
                        verticalStep = 1;
                        horizontalStep = 0;
                    }
                    map[currentY][currentX] = 'c';
                    break;
                case 'F':
                    if (verticalStep == -1) {
                        verticalStep = 0;
                        horizontalStep = 1;
                    } else if (horizontalStep == -1) {
                        verticalStep = 1;
                        horizontalStep = 0;

                    }
                    map[currentY][currentX] = 'o';
                    break;
                default:
                    System.out.println(map[currentY][currentX]);
                    throw new RuntimeException();

            }
            currentX += horizontalStep;
            currentY += verticalStep;
        }

        int counter = 0;
        for (int i = 0; i < map.length; i++) {
            boolean isOutside = true;
            for (int j = 0; j < map[i].length; j++) {
                if (!(map[i][j] >= 'a' && map[i][j] <= 'z') && !isOutside) {
                    int erg = countIfEnclosed(map, j, i);
                    if(erg > 0){
                        counter += erg;
                    }
                }
                if(map[i][j] == 'o'){
                    isOutside = false;
                }
                if(map[i][j] == 'c'){
                    isOutside = true;
                }
                if(map[i][j] == 's'){
                    isOutside = !isOutside;
                }
            }
        }

        return counter/2;
    }


    private static void printArray(char[][] inputArray) {
        if (inputArray != null) {
            for (char[] arr : inputArray) {
                for (char val : arr) {
                    System.out.print(val);
                }
                System.out.println();
            }
            System.out.println();
        }
    }

    public int countIfEnclosed(char[][] map, int currentX, int currentY) {
        if (currentY < 0 || currentY >= map.length || currentX < 0 || currentX >= map[currentY].length) {
            return Integer.MIN_VALUE/100000;
        }
        if (map[currentY][currentX] == 'v') {
            return 0;
        }
        if (map[currentY][currentX] == 'p' || map[currentY][currentX] == 'o'
                || map[currentY][currentX] == 'c' || map[currentY][currentX] == 's') {
            return 0;
        }
        map[currentY][currentX] = 'v';
        return 1 + countIfEnclosed(map, currentX + 1, currentY)
                + countIfEnclosed(map, currentX - 1, currentY)
                + countIfEnclosed(map, currentX, currentY + 1)
                + countIfEnclosed(map, currentX, currentY - 1);
        }

    public static void main(String[] args) {
        Day10 d10 = new Day10();
        System.out.println(d10.part1_findFurthestFromStart());
        System.out.println(d10.part2_findEnclosed());
    }
}
