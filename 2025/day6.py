from unittest import case


def part1():
  p = list()
  with open('day6_input.txt') as f:
    lines = f.readlines()
    for line in lines:
      p.append(line.split(" "))

  # cleanup input
  outer = list()
  for problem in p:
    inner = list()
    for c in problem:
      if c.strip() != '':
        inner.append(c.strip())
    outer.append(inner)
  p = outer


  sum = 0
  for i in range(len(p[0])):
    operation = p[-1][i]
    calculation = int(p[0][i])
    for j in range(1, len(p) - 1):
      cur_num = int(p[j][i])
      match operation:
        case '+': calculation += cur_num
        case '*': calculation *= cur_num

    sum += calculation

  return sum

class Problem:
  def __init__(self, numbers: list[list], operation: str):
    self.numbers = numbers
    self.operation = operation
    self.current = 0

  def __str__(self):
    return str(self.numbers) + ' ' + str(self.operation)

  def getNext(self):
    if self.current == len(self.numbers[0]):
      return None

    number = ""
    for i in range(len(self.numbers)):
      number += self.numbers[i][self.current]

    self.current += 1
    return int(number)

  def calculate(self):
    match self.operation:
      case '+': sum = 0
      case '*': sum = 1

    cur = self.getNext()
    while cur is not None:
      match self.operation:
        case '+': sum += cur
        case '*': sum *= cur
      cur = self.getNext()
    return sum


def part2():
  problems = list()
  with open('day6_input.txt') as f:
    problems = f.readlines()

  problems_reformatted = list()
  prev_operator = 0
  i = 1
  while i < len(problems[0]):
    number_length = 0
    while i < len(problems[-1]) and problems[-1][i] == ' ':
      number_length += 1
      i += 1
    next_operator = i

    numbers = list()
    for problem in problems[:-1]:
      numbers.append(problem[prev_operator:next_operator-1])

    problems_reformatted.append(Problem(numbers, problems[-1][prev_operator]))
    prev_operator = next_operator
    i += 1

  sum = 0
  for problem in problems_reformatted:
    sum += problem.calculate()
  return sum


if __name__ == '__main__':


  print(part1())
  print(part2())
