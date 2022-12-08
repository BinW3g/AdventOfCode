
enemy_move_dict = {"A": "Rock", "B": "Paper", "C": "Scissors"}
move_value = {"Rock": 1, "Paper": 2, "Scissors": 3}
result_points = {"Win": 6, "Draw": 3, "Loss": 0}


def calc_my_score_strat_1():
    my_move_dict = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}
    moves = open("input.txt", "r")
    total_score = 0
    for move in moves:
        move = move.strip().split(" ") # [enemy move, second my move]
        enemy_move = enemy_move_dict[move[0]]
        my_move = my_move_dict[move[1]]

        total_score += move_value[my_move]
        if my_move == enemy_move:
            total_score += result_points["Draw"]
            continue
        match enemy_move:
            case "Rock": total_score += result_points["Win"] if my_move == "Paper" else result_points["Loss"]
            case "Paper": total_score += result_points["Win"] if my_move == "Scissors" else result_points["Loss"]
            case "Scissors": total_score += result_points["Win"] if my_move == "Rock" else result_points["Loss"]
    return total_score


def calc_my_score_strat_2():
    my_goal_dict = {"X": "Loss", "Y": "Draw", "Z": "Win"}
    moves = open("input.txt", "r")
    total_score = 0
    for move in moves:
        move = move.strip().split(" ")  # [enemy move, second my move]
        enemy_move = enemy_move_dict[move[0]]
        my_gaol = my_goal_dict[move[1]]

        total_score += result_points[my_gaol]

        if my_gaol == "Draw":
            total_score += move_value[enemy_move]
            continue

        match enemy_move:
            case "Rock":
                total_score += move_value["Paper"] if my_gaol == "Win" else move_value["Scissors"]
            case "Paper":
                total_score += move_value["Scissors"] if my_gaol == "Win" else move_value["Rock"]
            case "Scissors":
                total_score += move_value["Rock"] if my_gaol == "Win" else move_value["Paper"]
    return total_score


if __name__ == "__main__":
    print(calc_my_score_strat_1())
    print(calc_my_score_strat_2())
