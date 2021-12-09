

def count_1_4_7_8():
    f = open("input.txt", "r")
    count = 0
    for line in f:
        elements = line.strip().split(" | ")[1].split(" ")
        for element in elements:
            if len(element) == 2 or len(element) == 4 or len(element) == 3 or len(element) == 7:
                count += 1
    return count


def make_dictionary(input_nums):
    num_dictionary = dict()
    segment_3_or_6 = list()
    segment_2_or_4 = list()
    for num in input_nums:
        num = "".join(sorted(num))
        if len(num) == 2:
            num_dictionary[num] = "1"
            segment_3_or_6.append(num[0])
            segment_3_or_6.append(num[1])
        elif len(num) == 3:
            num_dictionary[num] = "7"
        elif len(num) == 4:
            num_dictionary[num] = "4"
            for char in num:
                if char != segment_3_or_6[0] and char != segment_3_or_6[1]:
                    segment_2_or_4.append(char)
        elif len(num) == 5 and ((segment_3_or_6[0] in num) == (segment_3_or_6[1] in num)) \
                and ((segment_2_or_4[0] in num) != (segment_2_or_4[1] in num)):
            num_dictionary[num] = "3"
        elif len(num) == 5 and ((segment_3_or_6[0] in num) != (segment_3_or_6[1] in num)) \
                and ((segment_2_or_4[0] in num) == (segment_2_or_4[1] in num)):
            num_dictionary[num] = "5"
        elif len(num) == 5 and ((segment_3_or_6[0] in num) != (segment_3_or_6[1] in num)) \
                and ((segment_2_or_4[0] in num) != (segment_2_or_4[1] in num)):
            num_dictionary[num] = "2"
        elif len(num) == 6 and ((segment_3_or_6[0] in num) != (segment_3_or_6[1] in num)) \
                and ((segment_2_or_4[0] in num) == (segment_2_or_4[1] in num)):
            num_dictionary[num] = "6"
        elif len(num) == 6 and ((segment_3_or_6[0] in num) == (segment_3_or_6[1] in num)) \
                and ((segment_2_or_4[0] in num) == (segment_2_or_4[1] in num)):
            num_dictionary[num] = "9"
        elif len(num) == 6 and ((segment_3_or_6[0] in num) == (segment_3_or_6[1] in num)) \
                and ((segment_2_or_4[0] in num) != (segment_2_or_4[1] in num)):
            num_dictionary[num] = "0"
        elif len(num) == 7:
            num_dictionary[num] = "8"
    return num_dictionary


def sum_of_output():
    f = open("input.txt", "r")
    erg_sum = 0
    for line in f:
        elements = line.strip().split(" | ")
        num_dictionary = make_dictionary(sorted(elements[0].split(" "), key=len))
        num_str = ""
        for erg in elements[1].split(" "):
            erg = "".join(sorted(erg))
            num_str += num_dictionary[erg]
        erg_sum += int(num_str)
    return erg_sum


def main():
    print(count_1_4_7_8())
    print(sum_of_output())


if __name__ == "__main__":
    main()