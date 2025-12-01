def part1(start: int):
  count0s = 0
  with open("day1_input.txt") as f:
    for move in f:
      number = int(move[1:])
      if move[0] == "R":
        start += number
      elif move[0] == "L":
        start -= number
      else:
        print("That should not happen")

      start = start % 100
      if start == 0:
        count0s += 1
  return count0s


def part2(start: int):
  count0s = 0
  with open("day1_input.txt") as f:
    for move in f:
      number = int(move[1:])
      if move[0] == "R":
        start += number
        while start > 99:
          start -= 100
          count0s += 1

      elif move[0] == "L":
        if start == 0:
          count0s -= 1
        start -= number

        while start < 0:
          start += 100
          count0s += 1

        if start == 0:
          count0s += 1

      else:
        print("That should not happen")


  return count0s


if __name__ == '__main__':
  print(part1(50))
  print(part2(50))
