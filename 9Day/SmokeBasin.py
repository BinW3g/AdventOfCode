import numpy


def read_input_with_border():
    lines = open("input.txt", "r").readlines()
    input_array = numpy.zeros((len(lines) + 2, len(lines[0]) + 1))
    for x in range(1, len(input_array) - 1):
        line = lines[x-1].strip()
        for y in range(1, len(input_array[0]) - 1):
            input_array[x][y] = int(line[y-1])

    for y in range(len(input_array[0])):
        input_array[0][y] = 20
        input_array[len(input_array)-1][y] = 20

    for x in range(len(input_array)):
        input_array[x][0] = 20
        input_array[x][len(input_array[x]) - 1] = 20
    return input_array


def read_input():
    lines = open("input.txt", "r").readlines()
    input_array = numpy.zeros((len(lines), len(lines[0])-1))
    for x in range(len(input_array)):
        line = lines[x].strip()
        for y in range(len(line)):
            if int(line[y]) == 9:
                input_array[x][y] = int(line[y])
            else:
                input_array[x][y] = 1
    return input_array


def find_low_points():
    level_array = read_input_with_border()
    risk_level_sum = 0
    for x in range(1, len(level_array)-1):
        for y in range(1, len(level_array[x])-1):
            if level_array[x+1][y] > level_array[x][y] < level_array[x-1][y] \
                    and level_array[x][y-1] > level_array[x][y] < level_array[x][y+1]:
                risk_level_sum += level_array[x][y] + 1
    return risk_level_sum


def find_basin_count(array, x_pos, y_pos):
    try:
        if x_pos == -1 or y_pos == -1 or array[x_pos][y_pos] == 9 or array[x_pos][y_pos] == -1:
            return 0
        else:
            count = 1
            array[x_pos][y_pos] = -1
            count += find_basin_count(array, x_pos+1, y_pos)
            count += find_basin_count(array, x_pos-1, y_pos)
            count += find_basin_count(array, x_pos, y_pos+1)
            count += find_basin_count(array, x_pos, y_pos-1)
            return count
    except IndexError:
        return 0

def find_basin_locations():
    level_array = read_input()
    basin_counts = list()
    for x in range(len(level_array)):
        for y in range(len(level_array[x])):
            if level_array[x][y] != -1 and level_array[x][y] != 9:
                basin_counts.append(find_basin_count(level_array, x, y))
    largest_basins = 1
    for i in range(3):
        largest_basins *= basin_counts.pop(basin_counts.index(max(basin_counts)))
    return largest_basins


def main():
    print(find_low_points())
    print(find_basin_locations())


if __name__ == "__main__":
    main()
