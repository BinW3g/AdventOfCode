
def read_graph():
    f = open("input.txt", "r")
    cave_graph = dict()
    for line in f.readlines():
        points = line.strip().split("-")
        if points[0] not in cave_graph:
            cave_graph[points[0]] = dict()
        cave_graph[points[0]][points[1]] = 0

        if points[1] not in cave_graph:
            cave_graph[points[1]] = dict()
        cave_graph[points[1]][points[0]] = 1
    return cave_graph


def find_all_paths_big_caves_infinite(cave_graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in cave_graph:
        return []
    paths = []
    for node in cave_graph[start]:
        if node.isupper() or node not in path:
            new_paths = find_all_paths_big_caves_infinite(cave_graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths


def find_all_paths_small_cave_twice(cave_graph, start, end, path=[], has_small_twice=False):
    path = path + [start]
    if start == end:
        return [path]
    if start not in cave_graph:
        return []
    paths = []
    if path == ['start','A','b','A','c','A']:
        print(path)
    for node in cave_graph[start]:
        if node.isupper() or node not in path or \
                (str(node).islower() and node in path and not has_small_twice and node != 'start' and node != 'end'):
            if str(node).islower() and node in path and not has_small_twice:
                new_paths = find_all_paths_small_cave_twice(cave_graph, node, end, path, True)
            else:
                new_paths = find_all_paths_small_cave_twice(cave_graph, node, end, path, has_small_twice)

            for new_path in new_paths:
                paths.append(new_path)
    return paths


if __name__ == "__main__":
    all_paths = find_all_paths_big_caves_infinite(read_graph(), 'start', 'end')
    print(len(all_paths))
    all_paths = find_all_paths_small_cave_twice(read_graph(), 'start', 'end')
    print(len(all_paths))

