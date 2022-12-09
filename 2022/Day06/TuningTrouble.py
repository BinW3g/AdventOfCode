def find_start_of_packet_marker():
    message = open("input.txt", "r").read()

    for index in range(len(message) - 4):
        subsequence = message[index:index + 4]
        passed = True
        for char in subsequence:
            if subsequence.count(char) > 1:
                passed = False
                break
        if passed:
            return index + 4


def find_start_of_message_marker():
    message = open("input.txt", "r").read()

    for index in range(len(message) - 14):
        subsequence = message[index:index + 14]
        passed = True
        for char in subsequence:
            if subsequence.count(char) > 1:
                passed = False
                break
        if passed:
            return index + 14


if __name__ == '__main__':
    print(find_start_of_packet_marker())
    print(find_start_of_message_marker())
