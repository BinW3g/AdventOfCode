import numpy as np


def count_flashes(is_no_limit):
    population = np.genfromtxt("input.txt", dtype=int, delimiter=1)
    population = np.pad(population, pad_width=1, mode='constant', constant_values=-1)
    flash_count = 0
    i = 0
    while is_no_limit or i < 100:
        population[1:-1, 1:-1] += 1
        changed = True
        while changed:
            change_indexes = np.argwhere(population > 9)
            if change_indexes.size == 0:
                changed = False
                continue
            for x in range(len(change_indexes)):
                population[change_indexes[x][0]-1:change_indexes[x][0]+2, change_indexes[x][1]-1:change_indexes[x][1]+2] += 1
                population[change_indexes[x][0], change_indexes[x][1]] = -1000
                flash_count += 1
        population[population < 0] = 0
        if is_no_limit and np.sum(population[1:-1, 1:-1]) == 0:
            return i + 1
        population = np.pad(population[1:-1, 1:-1], pad_width=1, mode='constant', constant_values=-1)
        i += 1
    return flash_count


def main():
    print(count_flashes(False))
    print(count_flashes(True))


if __name__ == "__main__":
    main()

