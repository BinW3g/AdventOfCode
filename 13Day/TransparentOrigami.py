import numpy


def read_input():
    f = open("input.txt", "r")
    fold_values = list()
    dots = list()
    read_fold = False
    x_max = 0
    y_max = 0
    for line in f.readlines():
        if not line.strip():
            read_fold = True
            continue
        if read_fold:
            tokens = line.strip().split('=')
            fold_values.append([tokens[0][-1], int(tokens[1])])
        else:
            new_dot = list(map(int, line.strip().split(",")))
            dots.append(new_dot)
            if x_max < new_dot[1]:
                x_max = new_dot[1]
            if y_max < new_dot[0]:
                y_max = new_dot[0]

    array = numpy.zeros((x_max+1, y_max+1))
    for dot in dots:
        array[dot[1], dot[0]] = 1
    return array, fold_values


def fold_at(dots, axis, value):
    if axis == 'x':
        new_dots = numpy.zeros((len(dots), len(dots[0]) // 2))
        for dot in numpy.argwhere(dots != 0):
            if dot[1] > value:
                new_dots[dot[0], value - (dot[1] - value)] = 1
            else:
                new_dots[dot[0], dot[1]] = 1
    else:
        new_dots = numpy.zeros((len(dots) // 2, len(dots[0])))
        for dot in numpy.argwhere(dots != 0):
            if dot[0] > value:
                new_dots[value - (dot[0] - value), dot[1]] = 1
            else:
                new_dots[dot[0], dot[1]] = 1
    return new_dots


def print_array(array):
    for line in array:
        for value in line:
            if value == 0:
                print(".", end="")
            else:
                print("#", end="")
        print()
    print()


def get_empties_count_after_first_fold():
    input_values = read_input()
    dots = input_values[0]
    fold_values = input_values[1]
    dots = fold_at(dots, fold_values[0][0], fold_values[0][1])
    return numpy.count_nonzero(dots != 0)


def find_code():
    input_values = read_input()
    dots = input_values[0]
    fold_values = input_values[1]
    for fold in fold_values:
        dots = fold_at(dots, fold[0], fold[1])
    return dots


if __name__ == "__main__":
    print(str(get_empties_count_after_first_fold()))
    print_array(find_code())
