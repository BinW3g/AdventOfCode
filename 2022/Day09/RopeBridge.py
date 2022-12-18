import numpy as np
from operator import add

def calculate_robe_with_2_knot():
    moves = open("input.txt", "r")
    head_pos = [500, 0]
    tail_pos = [500, 0]
    places_visited = 1
    area = np.zeros((1000, 1000), dtype=int)
    area[9, 0] = 1
    for move in moves:
        tokens = move.strip().split(" ")
        for turn in range(int(tokens[1])):
            old_head_pos = head_pos.copy()
            match tokens[0]:
                case "U":
                    head_pos[0] -= 1
                case "D":
                    head_pos[0] += 1
                case "R":
                    head_pos[1] += 1
                case "L":
                    head_pos[1] -= 1
            if not head_pos[0] - 1 <= tail_pos[0] <= head_pos[0] + 1 \
                    or not head_pos[1] - 1 <= tail_pos[1] <= head_pos[1] + 1:
                tail_pos = old_head_pos
                if area[tail_pos[0], tail_pos[1]] == 0:
                    area[tail_pos[0], tail_pos[1]] = 1
                    places_visited += 1
    return places_visited


def calculate_robe_with_x_knot(knot_count):
    moves = open("input.txt", "r")
    knots = list()
    for x in range(knot_count):
        knots.append([5000, 5000])
    places_visited = 1
    area = np.zeros((10000, 10000), dtype=int)
    area[5000, 5000] = 1
    for move in moves:
        tokens = move.strip().split(" ")

        for turn in range(int(tokens[1])):
            match tokens[0]:
                case "U":
                    move = [-1, 0]
                case "D":
                    move = [1, 0]
                case "R":
                    move = [0, 1]
                case "L":
                    move = [0, -1]
            knots[0] = list(map(add, knots[0], move))
            for i in range(1, len(knots)):
                if not knots[i-1][0] - 1 <= knots[i][0] <= knots[i-1][0] + 1 \
                        or not knots[i-1][1] - 1 <= knots[i][1] <= knots[i-1][1] + 1:
                    if knots[i-1][1] == knots[i][1]:
                        if knots[i-1][0] < knots[i][0]:
                            knots[i] = [knots[i][0] + 1, knots[i][1]]
                        elif knots[i-1][0] > knots[i][0]:
                            knots[i] = [knots[i][0] - 1, knots[i][1]]
                    if knots[i-1][0] == knots[i][0]:
                        if knots[i-1][1] < knots[i][1]:
                            knots[i] = [knots[i][0], knots[i][1] + 1]
                        elif knots[i-1][1] > knots[i][1]:
                            knots[i] = [knots[i][0], knots[i][1] - 1]

                    if move[0] != 0:
                        if knots[i-1][1] < knots[i][1]:
                            knots[i] = [knots[i][0], knots[i][1] - 1]
                        elif knots[i-1][1] > knots[i][1]:
                            knots[i] = [knots[i][0], knots[i][1] + 1]
                    elif move[1] != 0:
                        if knots[i - 1][0] < knots[i][0]:
                            knots[i] = [knots[i][0] - 1, knots[i][1]]
                        elif knots[i - 1][0] > knots[i][0]:
                            knots[i] = [knots[i][0] + 1, knots[i][1]]

                    if i == len(knots)-1 and area[knots[i][0], knots[i][1]] == 0:
                        area[knots[i][0], knots[i][1]] = 1
                        places_visited += 1
    return places_visited


if __name__ == '__main__':
    print(calculate_robe_with_2_knot())
    print(calculate_robe_with_x_knot(2))
    print(calculate_robe_with_x_knot(10))
