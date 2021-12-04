def read_increase():
    f = open("input.txt", "r")
    increase = 0
    old_value = f.readline()
    for line in f:
        if int(old_value) < int(line):
            increase += 1
        old_value = line
    return increase


def read_increase_of_3():
    f = open("input.txt", "r")
    increase = 0
    value_list = [int(f.readline()), int(f.readline()), int(f.readline())]
    old_sum = 0
    for i in value_list:
        old_sum += i

    for line in f:
        value_list.pop(0)
        value_list.append(int(line))
        new_sum = 0

        for i in value_list:
            new_sum += i

        if old_sum < new_sum:
            increase += 1

        old_sum = new_sum
    return increase


print(read_increase())
print(read_increase_of_3())



