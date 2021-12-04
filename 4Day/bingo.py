import numpy as np


def make_result(board, last_number):
    result_sum = 0
    for x in board:
        for y in x:
            if y != -1:
                result_sum += y
    return result_sum * last_number


def init_boards():
    f = open("input.txt", "r")
    number_draw_order = list(map(int, f.readline().split(',')))
    f.readline()
    all_lines = f.readlines()

    # init
    all_pingo_boards = np.zeros((len(all_lines) // 6 + 1, 5, 5))
    x = 0
    y = 0
    z = 0
    for line in all_lines:
        line = line.rstrip('\n')
        if line:
            numbers = line.split(" ")
            for n in numbers:
                if n:
                    all_pingo_boards[x][y][z] = n
                    z += 1
        else:
            y = -1
            x += 1
        y += 1
        z = 0
    return all_pingo_boards, number_draw_order


def find_first_winner():
    result = init_boards()
    all_pingo_boards = result[0]
    number_draw_order = result[1]
    x = -1
    y = -1
    z = -1
    for drawn_number in number_draw_order:
        for board in all_pingo_boards:
            x += 1
            for line in board:
                y += 1
                for number in line:
                    z += 1
                    if number == drawn_number:
                        all_pingo_boards[x][y][z] = -1
                        # check if someone has pingo
                        if sum(all_pingo_boards[x][y]) == -5:
                            return make_result(board, number)
                        column_sum = 0
                        for check_line in board:
                            column_sum += check_line[z]
                        if column_sum == -5:
                            return make_result(board, number)
                z = -1
            y = -1
        x = -1


def board_is_finished(all_pingo_boards, x):
    for y in range(5):
        for z in range(5):
            all_pingo_boards[x][y][z] = -2


def find_last_winner():
    result = init_boards()
    all_pingo_boards = result[0]
    number_draw_order = result[1]
    last_winner = -1
    x = -1
    y = -1
    z = -1
    for drawn_number in number_draw_order:
        for board in all_pingo_boards:
            x += 1
            for line in board:
                y += 1
                for number in line:
                    z += 1
                    if number == drawn_number:
                        all_pingo_boards[x][y][z] = -1
                        # check if someone has pingo
                        if sum(all_pingo_boards[x][y]) == -5:
                            last_winner = make_result(board, number)
                            board_is_finished(all_pingo_boards, x)
                        column_sum = 0
                        for check_line in board:
                            column_sum += check_line[z]
                        if column_sum == -5:
                            last_winner = make_result(board, number)
                            board_is_finished(all_pingo_boards, x)
                z = -1
            y = -1
        x = -1
    return last_winner


print(find_first_winner())
print(find_last_winner())
