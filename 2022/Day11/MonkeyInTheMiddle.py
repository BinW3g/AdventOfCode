from tqdm import tqdm

monkey_items = list()
monkey_activity = list()
monkey_operation = list()
monkey_test_value = list()
monkey_throw_if_true = list()
monkey_throw_if_false = list()


def reset_input():
    global monkey_items
    global monkey_activity
    global monkey_operation
    global monkey_test_value
    global monkey_throw_if_true
    global monkey_throw_if_false
    monkey_items = list()
    monkey_activity = list()
    monkey_operation = list()
    monkey_test_value = list()
    monkey_throw_if_true = list()
    monkey_throw_if_false = list()


def parse_input():
    file = open("input.txt", "r")
    current_monkey = -1
    for line in file:
        tokens = line.strip().split(" ")
        match tokens[0]:
            case "Monkey":
                current_monkey += 1
                monkey_items.append([])
                monkey_activity.append(0)

            case "Starting":
                for item in tokens[2:]:
                    monkey_items[current_monkey].append(int(item.replace(",", "")))

            case "Operation:":
                if tokens[-1] == "old":
                    monkey_operation.append(["**"])
                else:
                    monkey_operation.append([tokens[-2], int(tokens[-1])])

            case "Test:":
                monkey_test_value.append(int(tokens[-1]))

            case "If":
                if tokens[1] == "true:":
                    monkey_throw_if_true.append(int(tokens[-1]))
                else:
                    monkey_throw_if_false.append(int(tokens[-1]))


def find_most_active_monkey(rounds, worry_level_divider):
    global monkey_items
    global monkey_activity
    global monkey_operation
    global monkey_test_value
    global monkey_throw_if_true
    global monkey_throw_if_false

    for i in tqdm(range(rounds)):
        for current_monkey, items in enumerate(monkey_items):
            for j in range(len(items)):
                item = items.pop(0)
                monkey_activity[current_monkey] += 1
                match monkey_operation[current_monkey][0]:
                    case "**":
                        item = item**2
                    case "+":
                        item += monkey_operation[current_monkey][1]
                    case "*":
                        item *= monkey_operation[current_monkey][1]
                item = item//worry_level_divider
                if item % monkey_test_value[current_monkey] == 0:
                    monkey_items[monkey_throw_if_true[current_monkey]].append(item)
                else:
                    monkey_items[monkey_throw_if_false[current_monkey]].append(item)

    max_monkey_business = max(monkey_activity)
    monkey_activity.remove(max_monkey_business)
    max2_monkey_business = max(monkey_activity)
    return max2_monkey_business * max_monkey_business


if __name__ == '__main__':
    parse_input()
    print(find_most_active_monkey(20, 3))
    reset_input()
    parse_input()
    print()
    print(find_most_active_monkey(10000, 1))
