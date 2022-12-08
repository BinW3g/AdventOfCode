def read_input():
    f = open("input.txt", "r")
    return list(map(int, f.readline().split(",")))


def calc_best_position(puzzel1):
    crabs = read_input()
    nearest_crab = min(crabs)
    furthest_crab = max(crabs)

    smallest_sum = 0
    for i in range(nearest_crab, furthest_crab):
        current_sum = 0
        for pos in crabs:
            steps = abs(pos - i)
            if puzzel1:
                current_sum += steps
            else:
                current_sum += int((steps + 1) * (steps / 2))

        if smallest_sum == 0 or current_sum < smallest_sum:
            smallest_sum = current_sum

    return smallest_sum


def main():
    print(calc_best_position(True))
    print(calc_best_position(False))


if __name__ == "__main__":
    main()
