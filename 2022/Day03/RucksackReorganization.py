from string import ascii_lowercase

item_priority = {}


def init():
    counter = 1
    for letter_lower in ascii_lowercase:
        item_priority[letter_lower] = counter
        item_priority[letter_lower.upper()] = counter + 26
        counter += 1


def find_the_duplicates():
    rucksacks = open("input.txt", "r")
    priority_sum = 0
    for rucksack in rucksacks:
        rucksack = rucksack.strip()
        first_half = rucksack[:int(len(rucksack)/2)]
        second_half = rucksack[int(len(rucksack)/2):]

        for item in first_half:
            if item in second_half:
                priority_sum += item_priority[item]
                break
    return priority_sum


def find_the_badges():
    rucksacks = open("input.txt", "r")
    priority_sum = 0
    three_rucksacks = list()
    for rucksack in rucksacks:
        rucksack = rucksack.strip()
        three_rucksacks.append(rucksack)
        if len(three_rucksacks) == 3:
            three_rucksacks.sort(key=len)
            for item in three_rucksacks.pop(0):
                if item in three_rucksacks[0] and item in three_rucksacks[1]:
                    priority_sum += item_priority[item]
                    break
            three_rucksacks.clear()
    return priority_sum


if __name__ == "__main__":
    init()
    print(find_the_duplicates())
    print(find_the_badges())
