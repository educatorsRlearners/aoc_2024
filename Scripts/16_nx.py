# Source: https://github.com/fuglede/adventofcode/blob/master/2024/day16/solutions.py

import networkx as nx

input_file = "data/16_data.txt"

with open(input_file) as f:
    ls = f.read().strip().split("\n")

four_dir = (1, -1, 1j, -1j)

G = nx.DiGraph()

for i, l in enumerate(ls):
    for j, x in enumerate(l):
        if x == "#":
            continue
        z = i + 1j * j
        if x == "S":
            start = (z, 1j)
        if x == "E":
            end = z
        for dz in four_dir:
            G.add_node((z, dz))

for z, dz in G.nodes:
    if (z + dz, dz) in G.nodes:
        G.add_edge((z, dz), (z + dz, dz), weight=1)
    for rot in -1j, 1j:
        G.add_edge((z, dz), (z, dz * rot), weight=1000)

for dz in four_dir:
    G.add_edge((end, dz), "end", weight=0)

# Part 1
print(nx.shortest_path_length(G, start, "end", weight="weight"))


# Part 2: Calculate the number of unique positions visited in all shortest paths
unique_positions = set()

# Iterate over all shortest paths
for path in nx.all_shortest_paths(G, start, "end", weight="weight"):
    # Iterate over each position in the path, excluding the last node
    for z, _ in path[:-1]:
        unique_positions.add(z)


# Print the number of unique positions
print(len(unique_positions))
