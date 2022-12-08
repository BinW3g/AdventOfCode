import numpy as np
from queue import PriorityQueue

# =============================================================================
# def enlarge(maze_original, new_size):
#     rows_orig, cols_orig = maze_original.shape
#
#     maze = np.append(maze_original, maze_original + 1, axis=1)
#
#     for i in range(2, new_size):
#         maze = np.append(maze, maze_original + i, axis=1)
#
#     for i in range(1, new_size):
#         maze = np.append(maze, maze[:rows_orig,:] + i, axis=0)
#
#     maze[maze > 9] %= 9
#
#     return maze
# =============================================================================

maze = np.genfromtxt("input.txt", delimiter=1, dtype=np.uint16)
# maze = enlarge(maze, 5)
maze = np.block([[(maze + i + j - 1) % 9 + 1 for i in range(5)] for j in range(5)])


def dijkstra(m, start, goal):
    rows, cols = m.shape
    frontier = PriorityQueue()

    frontier.put((0, start))
    visited = {start}

    while frontier:
        curr_risk, (i, j) = frontier.get()
        neighbors = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]

        # if current cell is the goal cell, return the risk
        if i == goal[0] and j == goal[1]:
            return curr_risk

        # check neighbors
        for row, col in neighbors:
            if 0 <= row < rows and 0 <= col < cols and (row, col) not in visited:
                risk = m[row, col]
                frontier.put((curr_risk + risk, (row, col)))
                visited.add((row, col))


rows, cols = maze.shape
print(dijkstra(maze, (0, 0), (rows - 1, cols - 1)))