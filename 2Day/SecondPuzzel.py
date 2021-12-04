def current_position():
    f = open("input.txt", "r")
    deep = 0
    horizontal = 0
    for line in f:
        tokens = line.split(" ")
        if tokens[0] == 'forward':
            horizontal += int(tokens[1])
        elif tokens[0] == 'down':
            deep += int(tokens[1])
        elif tokens[0] == 'up':
            deep -= int(tokens[1])

    return deep * horizontal

def current_position_part2():
    f = open("input.txt", "r")
    deep = 0
    horizontal = 0
    aim = 0
    for line in f:
        tokens = line.split(" ")
        if tokens[0] == 'forward':
            horizontal += int(tokens[1])
            deep += aim * int(tokens[1])
        elif tokens[0] == 'down':
            aim += int(tokens[1])
        elif tokens[0] == 'up':
            aim -= int(tokens[1])

    return deep * horizontal


print(current_position())
print(current_position_part2())