total_signal_strength = 0
cycle = 0
crt_row_pixels = ""


def execute_calculation():
    commands = open("input.txt", "r")
    x_signal_strength = 1
    for command in commands:
        tokens = command.strip().split(" ")

        match tokens[0]:
            case "noop":
                next_cycle(x_signal_strength)
            case "addx":
                next_cycle(x_signal_strength)
                next_cycle(x_signal_strength)
                x_signal_strength += int(tokens[1])
    print("".join(crt_row_pixels))


def next_cycle(signal_strength):
    global total_signal_strength
    global cycle
    global crt_row_pixels
    cycle += 1
    if (cycle - 20) % 40 == 0:
        total_signal_strength += cycle * signal_strength

    if cycle % 40 == 1:
        print("".join(crt_row_pixels))
        crt_row_pixels = [" "] * 40

    draw_pixel = (cycle - 1) % 40
    if signal_strength - 1 <= draw_pixel <= signal_strength + 1:
        crt_row_pixels[draw_pixel] = "#"


if __name__ == '__main__':
    execute_calculation()
    print(total_signal_strength)
