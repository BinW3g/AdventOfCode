

def read_stacks():
    lines = open("input.txt", "r")

    first_line = True
    for line in lines:
        if first_line:
            stacks = [[] for i in range(int(len(line) / 4))]
            first_line = False
        if "1" in line:
            break
        current_stack = 0
        for index in range(0, len(line), 4):
            container = line[index+1].strip()
            if container:
                stacks[current_stack].insert(0, container)
            current_stack += 1
    return stacks


def find_end_result_old_crane():
    stacks = read_stacks()
    moves = open("input.txt", "r")
    for move in moves:
        if move[0] != "m":
            continue
        tokens = move.split(" ")
        move_amount = int(tokens[1])
        move_from = int(tokens[3]) - 1
        move_to = int(tokens[5]) - 1

        for index in range(0, move_amount):
            container = stacks[move_from].pop()
            stacks[move_to].append(container)

    result = ""
    for stack in stacks:
        result += stack.pop()
    return result


def find_end_result_new_crane():
    stacks = read_stacks()
    moves = open("input.txt", "r")
    for move in moves:
        if move[0] != "m":
            continue
        tokens = move.split(" ")
        move_amount = int(tokens[1])
        move_from = int(tokens[3]) - 1
        move_to = int(tokens[5]) - 1

        containers = stacks[move_from][-move_amount:]
        stacks[move_from] = stacks[move_from][:-move_amount]
        stacks[move_to].extend(containers)

    result = ""
    for stack in stacks:
        result += stack.pop()
    return result


if __name__ == "__main__":
    print(find_end_result_old_crane())
    print(find_end_result_new_crane())
