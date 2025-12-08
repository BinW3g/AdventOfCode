import math
import numpy as np


def calcDistance(point1, point2):
  x = (point1[0]-point2[0])**2
  y = (point1[1]-point2[1])**2
  z = (point1[2]-point2[2])**2

  return math.sqrt(x + y + z)

def isConnected(point1, point2, circuits):
  for circuit in circuits:
    if point1 in circuit and point2 in circuit:
      return True
  return False

def part1(junctions):
  circuits = list()
  for i in range(1000):
    shortest = float('inf')
    closest = list()

    for j in range(len(junctions)):
      for k in range(j+1, len(junctions)):
        junction1 = junctions[j]
        junction2 = junctions[k]
        if calcDistance(junction1, junction2) < shortest \
            and not isConnected(junction1, junction2, circuits):
          shortest = calcDistance(junction1, junction2)
          closest = [junction1, junction2]

    circuits.append(closest)

  sorted_circuits = sorted(circuits, key=lambda circuit: len(circuit), reverse=True)
  return len(sorted_circuits[0]) * len(sorted_circuits[1]) * len(sorted_circuits[2])

def part2():
  pass

if __name__ == '__main__':
  with open('day8_input.txt') as f:
    input_values = f.read().split("\n")

  points = list()
  for line in input_values:
    points.append(list(map(int, line.split(","))))


  print(part1(points))
  print(part2())