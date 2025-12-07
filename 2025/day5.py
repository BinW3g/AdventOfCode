

def part1(ranges, ids):
  fresh_counter = 0
  for id in ids:
    for cur_range in ranges:
      if cur_range[0] <= id <= cur_range[1]:
        fresh_counter += 1
        break

  return fresh_counter

class Range:
  def __init__(self,start,end):
    self.start = start
    self.end = end

  # is other obsolete
  def improve(self, other):
    changed = False
    # other is completely inside this range
    if (self.start <= other.start <= self.end
        and self.start <= other.end <= self.end):
      return True

    # this start inside other Range
    if other.start <= self.start <= other.end:
      self.start = other.start
      changed = True

    # this end inside other Range
    if other.start <= self.end <= other.end:
      self.end = other.end
      changed = True

    return changed

  def __str__(self):
    return str(self.start) + '-' + str(self.end)


def part2(ranges):
  range_class = list()
  # parse to class
  for cur_range in ranges:
    range_class.append(Range(cur_range[0],cur_range[1]))

  updated = True
  while updated:
    updated = False
    new_ranges = list()
    for i,range1 in enumerate(range_class):
      improved = False
      for range2 in range_class[i+1:]:
        if range1.improve(range2):
          new_ranges.append(range1)
          range_class.remove(range2)
          improved = True
          updated = True
          break

      if not improved:
        new_ranges.append(range1)


    range_class = new_ranges

  range_sum = 0
  for cur_range in range_class:
    range_sum += (cur_range.end - cur_range.start) + 1

  return range_sum

# that part was solved with the help of https://dilipkumar.medium.com/interval-coding-pattern-068c36197cf5
class RangeNew:
  def __init__(self,start,end):
    self.start = start
    self.end = end

def isOverlapping(a: RangeNew, b: RangeNew):
  if a.start > b.start:
    return isOverlapping(b, a)
  if a.end < b.start:
    return False
  return True

def merge(a, b):
    a.start = min(a.start, b.start)
    a.end = max(a.end, b.end)

def part2_with_blog(ranges):
  ranges = sorted(ranges, key=lambda r: r[0])

  range_class = list()
  for cur_range in ranges:
    range_class.append(Range(cur_range[0],cur_range[1]))

  ans = [range_class[0]]
  for b in range_class[1:]:
    a = ans[-1]
    if isOverlapping(a, b):
      merge(a, b)
    else:
      ans.append(b)

  range_sum = 0
  for cur_range in ans:
    range_sum += (cur_range.end - cur_range.start) + 1

  return range_sum


def input_parser():
  ranges = list()
  ids = list()
  with open('day5_input.txt') as f:
    is_range = True
    for line in f:
      if line == '\n':
        is_range = False
        continue

      if is_range:
        bounds = line.split('-')
        ranges.append([int(bounds[0]), int(bounds[1])])
        continue
      else:
        ids.append(int(line))
  return ranges, ids

if __name__ == '__main__':
    input_ranges, input_ids = input_parser()
    print(part1(input_ranges, input_ids))
    print(part2(input_ranges))
    print(part2_with_blog(input_ranges))