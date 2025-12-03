import numpy as np

def part1(banks):
  jolt_sum = 0
  for bank in banks:
    max_jolt = 0
    for i in range(len(bank)-1):
      for j in range(i+1, len(bank)):
        jolt = int(bank[i] + bank[j])
        max_jolt = max(max_jolt, jolt)
    jolt_sum += max_jolt

  return jolt_sum

def part2(banks):
  jolt_sum = 0
  for bank in banks:
    bank_numbers = [int(c) for c in bank]
    indexes = list()
    indexes.append(np.argmax(bank_numbers[:-12]))
    for i in range(1,11):
      start_index = (indexes[-1]+1)
      indexes.append(start_index+np.argmax(bank_numbers[start_index:-(11-i)]))

    indexes.append((indexes[-1]+1)+np.argmax(bank_numbers[(indexes[-1]+1):]))
    number_str = "".join([bank[index] for index in indexes])
    jolt_sum += int(number_str)
  return jolt_sum


if __name__ == '__main__':
  banks = open('day3_input.txt').read().splitlines()
  print(part1(banks))
  print(part2(banks))


