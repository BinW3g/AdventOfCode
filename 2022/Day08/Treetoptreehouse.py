import numpy as np

treeline = np.genfromtxt("input.txt", delimiter=1)


def count_trees_that_can_be_seen():
    rows, columns = treeline.shape
    tree_count = rows * 2 + columns * 2 - 4

    for row_i in range(1, rows - 1):
        for col_i in range(1, columns - 1):
            if check_visibility(col_i, treeline[row_i, :]) \
                    or check_visibility(row_i, treeline[:, col_i]):
                tree_count += 1
    return tree_count


def check_visibility(index, tree_list):
    current_tree = tree_list[index]
    visible = True
    trees_to_right = tree_list[index + 1:]
    for tree in trees_to_right:
        if current_tree <= tree:
            visible = False
            break

    if not visible:
        visible = True
        trees_to_left = list(tree_list[:index])
        trees_to_left.reverse()
        for tree in trees_to_left:
            if current_tree <= tree:
                visible = False
                break
    return visible


def calculate_tree_science_score():
    rows, columns = treeline.shape
    max_tree_score = 0
    for row_i in range(1, rows - 1):
        for col_i in range(1, columns - 1):
            tree_score = check_visibility_distance(col_i, treeline[row_i, :]) \
                         * check_visibility_distance(row_i, treeline[:, col_i])
            if tree_score > max_tree_score:
                max_tree_score = tree_score
    return max_tree_score


def check_visibility_distance(index, tree_list):
    current_tree = tree_list[index]
    # trees visibility to the right
    trees_to_right = tree_list[index + 1:]
    visible_trees_right = 0
    for tree in trees_to_right:
        visible_trees_right += 1
        if current_tree <= tree:
            break

    # trees visibility to the left
    trees_to_left = list(tree_list[:index])
    trees_to_left.reverse()
    visible_trees_left = 0
    for tree in trees_to_left:
        visible_trees_left += 1
        if current_tree <= tree:
            break

    return visible_trees_right * visible_trees_left

if __name__ == '__main__':
    print(count_trees_that_can_be_seen())
    print(calculate_tree_science_score())
