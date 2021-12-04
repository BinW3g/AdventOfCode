def get_gamma_multiplied_by_epsilon():
    f = open("input.txt", "r")

    counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    count_lines = 0
    for line in f:
        count_lines += 1
        i = 0
        for char in line:
            if not char == "\n":
                counts[i] += int(char)
            i += 1

    erg_gamma = ""
    erg_epsilon = ""
    for count in counts:
        if count >= (count_lines / 2):
            erg_gamma += "1"
            erg_epsilon += "0"
        else:
            erg_gamma += "0"
            erg_epsilon += "1"
    return int(erg_gamma, 2) * int(erg_epsilon, 2)


def live_support_rating():
    f = open("input.txt", "r")
    count = 0
    all_lines_for_oxy = f.readlines()
    all_lines_for_co2 = all_lines_for_oxy.copy()
    position = 0
    while not len(all_lines_for_oxy) == 1:
        for line in all_lines_for_oxy:
            count += int(line[position])

        if count >= len(all_lines_for_oxy)/2:
            keep_all_with = "1"
        else:
            keep_all_with = "0"

        all_lines_for_oxy = list(filter(lambda x: x[position] == str(keep_all_with), all_lines_for_oxy))

        position += 1
        count = 0

    position = 0
    while not len(all_lines_for_co2) == 1:
        for line in all_lines_for_co2:
            count += int(line[position])

        if count < len(all_lines_for_co2)/2:
            keep_all_with = "1"
        else:
            keep_all_with = "0"

        all_lines_for_co2 = list(filter(lambda x: x[position] == str(keep_all_with), all_lines_for_co2))

        position += 1
        count = 0
    return int(all_lines_for_oxy[0], 2) * int(all_lines_for_co2[0], 2)


print(get_gamma_multiplied_by_epsilon())
print(live_support_rating())
