import math

def part1(tiles):
  tiles.sort(key=lambda x: math.sqrt((x[0]) ** 2 + (x[1]) ** 2))

  min_tile = tiles[0]
  max_tile = tiles[-1]

  return (max_tile[1] - min_tile[1] + 1) * (max_tile[0] - min_tile[0] + 1)


class Area:
  def __init__(self, a, b):
    if math.sqrt(a[0]**2 + a[1]**2) < math.sqrt(b[0]**2 + b[1]**2):
      self.a = a
      self.b = b
    else:
      self.a = b
      self.b = a

    self.area = (abs(b[1] - a[1]) + 1) * (abs(b[0] - a[0]) + 1)

  def isPointInArea(self, p):
    if (min(self.a[0], self.b[0]) < p[0] < max(self.a[0], self.b[0])
        and min(self.a[1], self.b[1]) < p[1] < max(self.a[1], self.b[1])):
      return True
    return False

  def __str__(self):
    return '(' + str(self.a) + ' ' + str(self.b) + ' ' + str(self.area) + ')'


def part2(tiles):
  areas = list()
  for i, tile in enumerate(tiles):
    for tile2 in tiles[i+1:]:
      areas.append(Area(tile, tile2))

  areas.sort(key=lambda x: x.area, reverse=True)
  for area in areas:
    found = True
    for tile in tiles:
      if area.isPointInArea(tile):
        found = False
        break
    if found:
      return area.area

  return -1

if __name__ == '__main__':
  positions = list()

  with open('day9_input.txt') as f:
    for line in f.readlines():
      positions.append(list(map(int, line.split(','))))

  print(part1(positions))
  print(part2(positions))