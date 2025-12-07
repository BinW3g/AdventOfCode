from idlelib.browser import transform_children


def part1(tachyon_manifold):

  lines = [list(x) for x in tachyon_manifold[1:]]

  beams = set()
  beams.add(tachyon_manifold[0].find("S"))
  split_counter = 0
  for line in lines:
    new_beams = set()
    for beam in beams:
      if line[beam] == '^':
        new_beams.add(beam-1)
        new_beams.add(beam+1)
        split_counter += 1
      else:
        line[beam] = "|"
        new_beams.add(beam)
    beams = new_beams

  # print("\n".join(["".join(line) for line in lines]))
  return split_counter


# recursive is too slow
def split(curr_beam, lines, curr_line):
  if curr_line >= len(lines):
    return 1

  if lines[curr_line][curr_beam] == '^':
    return (split(curr_beam+1, lines, curr_line+1)
            + split(curr_beam-1, lines, curr_line+1))
  else:
    return split(curr_beam, lines, curr_line+1)


def part2_recursive(tachyon_manifold):
  lines = [list(x) for x in tachyon_manifold[1:]]

  start_beam = tachyon_manifold[0].find("S")

  timeline_counter = split(start_beam, lines, 1)
  # print("\n".join(["".join(line) for line in lines]))
  return timeline_counter

def part2(tachyon_manifold):
  # todo implement a counter instead of beam therefore it counts with how many paths you reach the end
  lines_str = [list(x) for x in tachyon_manifold[1:]]

  lines = list()
  for line in lines_str:
    new_line = list()
    for c in line:
      if c != '.':
        new_line.append(c)
      else:
        new_line.append(0)
    lines.append(new_line)

  beams = set()
  start = tachyon_manifold[0].find("S")
  beams.add(start)
  lines[0][start] = 1
  for i, line in enumerate(lines[:-1]):
    new_beams = set()
    for beam in beams:
      cur_num = line[beam]
      if lines[i+1][beam] == '^':
        new_beams.add(beam - 1)
        new_beams.add(beam + 1)
        lines[i+1][beam+1] += cur_num
        lines[i+1][beam-1] += cur_num
      else:
        lines[i+1][beam] += cur_num
        new_beams.add(beam)
    beams = new_beams

  # print("\n".join(["".join(line) for line in lines]))
  return sum(lines[-1])


if __name__ == '__main__':
    manifold = open('day7_input.txt').read().split('\n')
    print(part1(manifold))
    print(part2(manifold))