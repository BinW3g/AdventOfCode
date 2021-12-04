import numpy as np


def make_result(board, last_number):
    result_sum = 0
    for x in board:
        for y in x:
            if y != -1:
                result_sum += y
    return result_sum * last_number


def is_pingo(board, y, z, check_into_direction, deep):
    if (0 <= y <= 4) and (0 <= z <= 4):
        is_set = board[y][z] == -1
        if is_set:
            deep += 1
            if check_into_direction == 'u':
                result = is_pingo(board, y - 1, z, check_into_direction, deep)
                return result[0], result[1]
            elif check_into_direction == 'd':
                result = is_pingo(board, y + 1, z, check_into_direction, deep)
                return result[0], result[1]
            elif check_into_direction == 'l':
                result = is_pingo(board, y, z - 1, check_into_direction, deep)
                return result[0], result[1]
            elif check_into_direction == 'r':
                result = is_pingo(board, y, z + 1, check_into_direction, deep)
                return result[0], result[1]
            elif check_into_direction == 'dtl':
                result = is_pingo(board, y - 1, z - 1, check_into_direction, deep)
                return result[0], result[1]
            elif check_into_direction == 'ddr':
                result = is_pingo(board, y + 1, z + 1, check_into_direction, deep)
                return result[0], result[1]
            elif check_into_direction == 'dtr':
                result = is_pingo(board, y - 1, z - 1, check_into_direction, deep)
                return result[0], result[1]
            elif check_into_direction == 'ddl':
                result = is_pingo(board, y + 1, z + 1, check_into_direction, deep)
                return result[0], result[1]
        else:
            return is_set, deep
    else:
        return True, deep


def init_boards():
    f = open("input.txt", "r")
    number_draw_order = list(map(int, f.readline().split(',')))
    f.readline()
    all_lines = f.readlines()

    # init
    all_pingo_boards = np.zeros((int(len(all_lines) / 6) + 1, 5, 5))
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
                        result1 = is_pingo(board, y, z, 'u', 0)
                        result2 = is_pingo(board, y, z, 'd', 0)
                        if result1[0] and result2[0] and result1[1] + result2[1] == 6:
                            return make_result(board, number)
                        result1 = is_pingo(board, y, z, 'l', 0)
                        result2 = is_pingo(board, y, z, 'r', 0)
                        if result1[0] and result2[0] and result1[1] + result2[1] == 6:
                            return make_result(all_pingo_boards[x], number)
                        result1 = is_pingo(board, y, z, 'dtl', 0)
                        result2 = is_pingo(board, y, z, 'ddr', 0)
                        if result1[0] and result2[0] and result1[1] + result2[1] == 6:
                            return make_result(board, number)
                        result1 = is_pingo(board, y, z, 'dtr', 0)
                        result2 = is_pingo(board, y, z, 'ddl', 0)
                        if result1[0] and result2[0] and result1[1] + result2[1] == 6:
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
                        result1 = is_pingo(board, y, z, 'u', 0)
                        result2 = is_pingo(board, y, z, 'd', 0)
                        if result1[0] and result2[0] and result1[1] + result2[1] == 6:
                            last_winner = make_result(board, number)
                            board_is_finished(all_pingo_boards, x)
                        result1 = is_pingo(board, y, z, 'l', 0)
                        result2 = is_pingo(board, y, z, 'r', 0)
                        if result1[0] and result2[0] and result1[1] + result2[1] == 6:
                            last_winner = make_result(board, number)
                            board_is_finished(all_pingo_boards, x)
                        result1 = is_pingo(board, y, z, 'dtl', 0)
                        result2 = is_pingo(board, y, z, 'ddr', 0)
                        if result1[0] and result2[0] and result1[1] + result2[1] == 6:
                            last_winner = make_result(board, number)
                            board_is_finished(all_pingo_boards, x)
                        result1 = is_pingo(board, y, z, 'dtr', 0)
                        result2 = is_pingo(board, y, z, 'ddl', 0)
                        if result1[0] and result2[0] and result1[1] + result2[1] == 6:
                            last_winner = make_result(board, number)
                            board_is_finished(all_pingo_boards, x)
                z = -1
            y = -1
        x = -1
    return last_winner


print(find_first_winner())
print(find_last_winner())
