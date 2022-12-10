directory_sizes = {"/": 0}


def read_dir_sizes():
    console_log = open("input.txt", "r")
    current_dir = []
    for line in console_log:
        tokens = line.strip().split(" ")
        if tokens[0] == "$":
            if tokens[1] == "cd":
                parameter = tokens[2]
                match parameter:
                    case "..": current_dir.pop()
                    case "/": current_dir = ["/"]
                    case _:
                        current_dir.append(parameter)
            elif tokens[1] == "ls":
                continue
        else:
            if tokens[0] == "dir":
                if not tokens[1] in directory_sizes:
                    dir_string = "/".join(current_dir) + "/" + tokens[1]
                    directory_sizes[dir_string] = 0
            else:
                for i in range(len(current_dir)):
                    directory_sizes["/".join(current_dir[:i+1])] += int(tokens[0])


def sum_of_directory_sizes_under_100000():
    result = 0
    for directory in directory_sizes:
        if directory_sizes[directory] <= 100000:
            result += directory_sizes[directory]
    return result


def find_size_of_directory_to_delete():
    total_space_available = 70000000
    total_space_used = directory_sizes["/"]
    update_size = 30000000
    space_to_free_up = total_space_used + update_size - total_space_available
    smallest_directory_to_delete = total_space_used
    for directory in directory_sizes:
        if space_to_free_up < directory_sizes[directory] < smallest_directory_to_delete :
            smallest_directory_to_delete = directory_sizes[directory]
    return smallest_directory_to_delete


if __name__ == '__main__':
    read_dir_sizes()
    print(sum_of_directory_sizes_under_100000())
    print(find_size_of_directory_to_delete())
