import time


class FishGroup:
    def __init__(self, fish, days):
        self.fish_count = fish
        self.days_left = days

    def count_down(self):
        self.days_left -= 1
        if self.days_left == -1:
            self.days_left = 6
            return self.fish_count
        return -1

    def add_fishes(self, fish):
        self.fish_count += fish

    def __str__(self):
        return str(self.fish_count) + " " + str(self.days_left)


def read_input():
    f = open("input.txt", "r")
    return list(map(int, f.readline().strip().split(",")))


# slow and easy
def evolution(lantern_evolution, days):
    for num in range(days):
        for i in range(len(lantern_evolution)):
            if lantern_evolution[i] == 0:
                lantern_evolution[i] = 7
                lantern_evolution.append(8)
            lantern_evolution[i] -= 1
        # print("After " + str(num) + " day: " + str(lantern_evolution))
    return len(lantern_evolution)


def fast_evolution(lantern_evolution, days):
    fish = [0, 0, 0, 0, 0, 0, 0]
    for num in lantern_evolution:
        if num == 0:
            fish[0] += 1
        elif num == 1:
            fish[1] += 1
        elif num == 2:
            fish[2] += 1
        elif num == 3:
            fish[3] += 1
        elif num == 4:
            fish[4] += 1
        elif num == 5:
            fish[5] += 1
        elif num == 6:
            fish[6] += 1
    fishes = list()
    new_fishes = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(fish)):
        fishes.append(FishGroup(fish[i], i))

    for i in range(days):
        new_fishes_count = new_fishes.pop(0)
        for fish in fishes:
            new_fish_count = fish.count_down()
            if new_fish_count != -1:
                fish.add_fishes(new_fishes_count)
                new_fishes.append(new_fish_count+new_fishes_count)

    fish_sum = 0
    for fish in fishes:
        fish_sum += fish.fish_count
    fish_sum += sum(new_fishes)
    return fish_sum


def main():
    current_evolution = read_input()
    print(str(evolution(current_evolution, 80)))

    current_evolution = read_input()
    print(str(fast_evolution(current_evolution, 80)))

    current_evolution = read_input()
    print(str(fast_evolution(current_evolution, 256)))


if __name__ == "__main__":
    main()
