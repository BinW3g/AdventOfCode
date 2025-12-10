import math

def part1(tiles):
  tiles.sort(key=lambda x: math.sqrt((x[0]) ** 2 + (x[1]) ** 2))

  min_tile = tiles[0]
  max_tile = tiles[-1]

  return (max_tile[1] - min_tile[1] + 1) * (max_tile[0] - min_tile[0] + 1)


def part2(tiles):
  pass

if __name__ == '__main__':
  positions = list()

  with open('day9_input.txt') as f:
    for line in f.readlines():
      positions.append(list(map(int, line.split(','))))

  print(part1(positions))
  print(part2(positions))