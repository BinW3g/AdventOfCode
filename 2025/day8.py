import math
import numpy as np
from functools import cmp_to_key

class Line:
  def __init__(self, a, b):
    self.a = a
    self.b = b
    self.distance = calcDistance(a, b)

  def __str__(self):
    return f"({self.a},{self.b})"

  def connecting(self, other):
    if self.a == other.a or self.b == other.b:
      return True
    return False

def calcDistance(point1, point2):
  x = (point1[0]-point2[0])**2
  y = (point1[1]-point2[1])**2
  z = (point1[2]-point2[2])**2

  return math.sqrt(x + y + z)

def createsCircel(circuit, line: Line):
  for i, l1 in enumerate(circuit):
    for l2 in circuit[i+1:]:
      if (line.a == l1.a and line.b == l2.b) or (line.a == l1.b and line.b == l2.a) :
        return True
  return False



def part1(junctions, n):
  lines = list()
  for i, p1 in enumerate(junctions):
    for p2 in junctions[i+1:]:
      lines.append(Line(p1, p2))

  lines.sort(key=lambda l: l.distance)

  circuits = list(list())
  i = 0
  circuits_created = 0
  while circuits_created < n:
    line = lines[i]
    inserted = False
    canceled = False
    for circuit in circuits:
      for l in circuit:
        if line.connecting(l):
          if createsCircel(circuit, line):
            canceled = True
            circuits_created -= 1
            break
          circuit.append(line)
          inserted = True
          break
      if inserted or canceled:
        break
    if not inserted:
      circuits.append([line])
    i += 1
    circuits_created += 1



  sorted_circuits = sorted(circuits, key=lambda circuit: len(circuit), reverse=True)
  return (len(sorted_circuits[0])+1) * (len(sorted_circuits[1])+1) * (len(sorted_circuits[2])+1)

def part2():
  pass

if __name__ == '__main__':
  with open('day8_input.txt') as f:
    input_values = f.read().split("\n")

  points = list()
  for line in input_values:
    points.append(list(map(int, line.split(","))))


  # print(part1(points, 10))
  print(part1(points, 1000))
  print(part2())