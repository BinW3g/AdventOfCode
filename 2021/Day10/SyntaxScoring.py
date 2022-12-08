open_brackets = "({[<"
open_to_close = {"(": ")", "[": "]", "{": "}", "<": ">", "": 0}


def find_block(line, index, errors):
    if index < len(line):
        if line[index] in open_brackets:
            closer_index = find_block(line, index + 1, errors)
            if closer_index == "":
                return ""
            if open_to_close[line[index]] != line[closer_index]:
                errors[line[closer_index]] += 1
            return find_block(line, closer_index + 1, errors)
        return index
    return ""


def remove_blocks(line):
    remove = True
    while remove:
        before_length = len(line)
        line = line.replace("()", "")
        line = line.replace("[]", "")
        line = line.replace("{}", "")
        line = line.replace("<>", "")
        if before_length == len(line):
            remove = False
    return line


def calc_syntax_score():
    f = open("input.txt", "r")

    errors = {")": 0, "]": 0, "}": 0, ">": 0}
    for line in f.readlines():
        line = line.strip()
        find_block(line, 0, errors)

    error_score = 0
    error_score_dic = {")": 3, "]": 57, "}": 1197, ">": 25137}
    for key in errors:
        error_score += error_score_dic[key] * errors[key]
    return error_score


def close_lines():
    f = open("input.txt", "r")

    completed_lines = list()
    for line in f.readlines():
        errors = {")": 0, "]": 0, "}": 0, ">": 0}
        line = line.strip()
        find_block(line, 0, errors)
        if sum(errors.values()) == 0:
            completed_lines.append(line)

    completion_score_dic = {"(": 1, "[": 2, "{": 3, "<": 4}
    completion_scores = list()
    for line in completed_lines:
        completion_score = 0
        line = remove_blocks(line)
        line = reversed(line)
        for char in line:
            completion_score *= 5
            completion_score += completion_score_dic[char]
        completion_scores.append(completion_score)

    return sorted(completion_scores).pop(len(completion_scores)//2)





def main():
    print(calc_syntax_score())
    print(close_lines())


if __name__ == "__main__":
    main()
