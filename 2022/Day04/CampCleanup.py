def count_completly_included_assignments():
    list_of_pairs = open("input.txt", "r")
    count = 0

    for pair in list_of_pairs:
        assignments = pair.strip().split(",")
        first_assignment =  list(map(int, assignments[0].split("-")))
        second_assignment = list(map(int, assignments[1].split("-")))
        if (first_assignment[0] <= second_assignment[0] and first_assignment[1] >= second_assignment[1]) \
                or (second_assignment[0] <= first_assignment[0] and second_assignment[1] >= first_assignment[1]):
            count += 1
            continue
    return count


def count_overlapping_assignments():
    list_of_pairs = open("input.txt", "r")
    count = 0

    for pair in list_of_pairs:
        assignments = pair.strip().split(",")
        first_assignment = list(map(int, assignments[0].split("-")))
        second_assignment = list(map(int, assignments[1].split("-")))
        if first_assignment[1] >= second_assignment[0] and second_assignment[1] >= first_assignment[0]:
            count += 1
            continue
    return count


if __name__ == "__main__":
    print(count_completly_included_assignments())
    print(count_overlapping_assignments())
