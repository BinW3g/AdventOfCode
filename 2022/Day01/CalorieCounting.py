
def count_calories_1():
    all_calories = open("input.txt", "r")
    most_calories = 0
    current_calories = 0
    for calorie in all_calories:
        if calorie != '\n':
            current_calories += int(calorie)
        else:
            if most_calories < current_calories:
                most_calories = current_calories
            current_calories = 0
    return most_calories


def count_calories_2():
    all_calories = open("input.txt", "r")
    top3_calories = [0,0,0]
    current_calories = 0
    for calorie in all_calories:
        if calorie != '\n':
            current_calories += int(calorie)
        else:
            if min(top3_calories) < current_calories:
                top3_calories.remove(min(top3_calories))
                top3_calories.append(current_calories)
            current_calories = 0
    return sum(top3_calories)


def main():
    print(count_calories_1())
    print(count_calories_2())


if __name__ == "__main__":
    main()
