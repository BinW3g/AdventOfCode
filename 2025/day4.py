import numpy as np

def part1(data):
  accessible = 0
  reformated = (data == "@") * 1
  reformated = np.pad(reformated, pad_width=(1,1))
  for i in range(1, reformated.shape[0] - 1):
    for j in range(1, reformated.shape[1] - 1):
      if reformated[i][j] != 1:
        continue
      if sum(reformated[i-1:i+2, j-1:j+2].flatten()) <= 4:
        accessible += 1
  return accessible

def part2(data):
  accessible = 0
  removed = True
  reformated = (data == "@") * 1
  reformated = np.pad(reformated, pad_width=(1, 1))
  while removed:
    removed = False
    for i in range(1, reformated.shape[0] - 1):
      for j in range(1, reformated.shape[1] - 1):
        if reformated[i][j] != 1:
          continue
        if sum(reformated[i - 1:i + 2, j - 1:j + 2].flatten()) <= 4:
          accessible += 1
          reformated[i, j] = 0
          removed = True

  return accessible

if __name__ == '__main__':
  with open('day4_input.txt') as f:
    data = f.read().splitlines()


  inp = np.array([list(d) for d in data])
  print(part1(inp))
  print(part2(inp))