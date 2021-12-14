from string import ascii_uppercase


def read_input():
    f = open("input.txt", "r")
    template = f.readline().strip()
    rules = dict()
    f.readline()

    for line in f.readlines():
        tokens = line.strip().split(" -> ")
        rules[tokens[0]] = tokens[1]
    return template, rules


# bad and slow but easy
def part_1():
    input_values = read_input()
    template = input_values[0]
    rules = input_values[1]

    for i in range(10):
        index = 0
        while index < len(template) - 1:
            if template[index:index + 2] in rules:
                template = template[:index + 1] + rules[template[index:index + 2]] + template[index + 1:]
                index += 1
            index += 1

    max_count = -1
    min_count = -1
    for char in ascii_uppercase:
        current_count = template.count(char)
        if (current_count < min_count or min_count == -1) and current_count != 0:
            min_count = current_count
        if current_count > max_count:
            max_count = current_count
    return max_count - min_count


def part_2(iterations):
    input_values = read_input()
    template = input_values[0]
    rules = input_values[1]
    count_letters = dict()

    for char in template:
        if char not in count_letters:
            count_letters[char] = 1
        else:
            count_letters[char] += 1

    pairs = dict()
    for index in range(len(template) - 1):
        pair = template[index:index + 2]
        if pair in pairs:
            pairs[pair] += 1
        else:
            pairs[pair] = 1

    for i in range(iterations):
        # create copy of pairs for iterating
        old_pairs = dict(pairs)
        for pair in old_pairs:
            # pair minus old pair
            pairs[pair] -= old_pairs[pair]
            if pairs[pair] == 0:
                pairs.pop(pair)
            # create new pairs
            rule_letter = rules[pair]
            new_pairs = [pair[0] + rule_letter, rule_letter + pair[1]]
            # count letters through creating pairs
            if rule_letter not in count_letters:
                count_letters[rule_letter] = old_pairs[pair]
            else:
                count_letters[rule_letter] += old_pairs[pair]
            # insert new pairs into pairs
            for new_pair in new_pairs:
                if new_pair in pairs:
                    pairs[new_pair] += old_pairs[pair]
                else:
                    pairs[new_pair] = old_pairs[pair]

    return max(count_letters.values()) - min(count_letters.values())


if __name__ == "__main__":
    print(part_2(10))
    print(part_2(40))
