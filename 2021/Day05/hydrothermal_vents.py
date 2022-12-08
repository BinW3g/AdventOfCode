import numpy as np


def draw_straight_line(clouds, from_x, to_x, from_y, to_y):
    if from_x > to_x:
        buffer = from_x
        from_x = to_x
        to_x = buffer

    if from_y > to_y:
        buffer = from_y
        from_y = to_y
        to_y = buffer

    for x in range(from_x, to_x+1):
        for y in range(from_y, to_y+1):
            clouds[x][y] += 1


def draw_diagonally_line(clouds, from_x, to_x, from_y, to_y):
    change_x = 1
    change_y = 1
    if from_x > to_x:
        change_x = -1

    if from_y > to_y:
        change_y = -1

    x = from_x
    y = from_y
    for i in range(abs(to_x - from_x)+1):
        clouds[x][y] += 1
        x += change_x
        y += change_y


def init_clouds(clouds, only_straight):
    f = open("input.txt", "r")

    for line in f.readlines():
        line = line.strip()
        coords = line.split(" -> ")
        coords[0] = list(map(int, coords[0].split(",")))
        coords[1] = list(map(int, coords[1].split(",")))
        if coords[0][0] == coords[1][0] or coords[0][1] == coords[1][1]:
            draw_straight_line(clouds, coords[0][1], coords[1][1], coords[0][0], coords[1][0])
        elif not only_straight:
            draw_diagonally_line(clouds, coords[0][1], coords[1][1], coords[0][0], coords[1][0])


def find_overlap_count(clouds, min_overlaps):
    count = 0
    for x in range(len(clouds)):
        for y in range(len(clouds[x])):
            if clouds[x][y] > min_overlaps:
                count += 1
    return count


# debugging only
def print_clouds(clouds):
    for x in range(len(clouds)):
        for y in range(len(clouds[x])):
            if clouds[x][y] == 0:
                print(".", end=" ")
            else:
                print(int(clouds[x][y]), end=" ")
        print()


def main():
    clouds = np.zeros((1000, 1000))
    init_clouds(clouds, True)
    print(find_overlap_count(clouds, 1))
    clouds = np.zeros((1000, 1000))
    init_clouds(clouds, False)
    print(find_overlap_count(clouds, 1))


if __name__ == "__main__":
    main()
