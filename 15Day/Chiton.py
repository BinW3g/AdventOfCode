import numpy as np


def sum_up(field, x, y, current_risk=0, path_risk=[]):
    if len(field)-1 == x and len(field[0])-1 == y:
        path_risk.append(current_risk)
        return path_risk
    current_risk += field[x][y]
    print("Currently at: ", str(x), str(y))
    if x != len(field)-1:
        sum_up(field, x+1, y, current_risk, path_risk)
    if y != len(field[0])-1:
        sum_up(field, x, y+1, current_risk, path_risk)
    return path_risk


def find_shortest_path():
    field = np.genfromtxt("input.txt", dtype=int, delimiter=1)
    return min(sum_up(field, 0, 0))


if __name__ == "__main__":
    print(find_shortest_path())
