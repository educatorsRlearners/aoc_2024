# Minimally modified from https://github.com/fuglede/adventofcode/blob/master/2024/day18/solutions.py

import networkx as nx

sample_input = "data/18_sample.txt"

input_file = "data/18_data.txt"

with open(input_file) as f:
    ns = [tuple(map(int, l.split(","))) for l in f.read().strip().split("\n")]

size_of_grid = max(max(ns))


if size_of_grid == 70:
    BYTES = 1023
else:
    BYTES = 11


def get_grid_space(size_of_grid):
    return nx.grid_2d_graph(size_of_grid + 1, size_of_grid + 1)


max_dist = (size_of_grid, size_of_grid)

G = get_grid_space(size_of_grid)


for i, p in enumerate(ns):
    G.remove_node(p)
    if i == BYTES:
        # Part 1
        print(nx.shortest_path_length(G, (0, 0), max_dist))
    elif not nx.has_path(G, (0, 0), max_dist):
        # Part 2
        print(p)
        break
