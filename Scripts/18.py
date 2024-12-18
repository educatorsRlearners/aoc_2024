import networkx as nx

sample_input = "data/18_sample.txt"

input_file = "data/18_data.txt"


sample_grid_space = 7
grid_space = 71


def get_grid_space(size_of_gride):
    return nx.grid_2d_graph(size_of_gride, size_of_gride)


def get_max_dist(grid_space):
    return (grid_space - 1, grid_space - 1)


with open(input_file) as f:
    ns = [tuple(map(int, l.split(","))) for l in f.read().strip().split("\n")]

G = get_grid_space(grid_space)

max_dist = get_max_dist(grid_space)

for i, p in enumerate(ns):
    G.remove_node(p)
    if i == 1023:
        # Part 1
        print(nx.shortest_path_length(G, (0, 0), max_dist))
    elif not nx.has_path(G, (0, 0), max_dist):
        # Part 2
        print(p)
        break
