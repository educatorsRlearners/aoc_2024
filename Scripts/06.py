input = "data/06_data.txt"


def get_solution(input):

    G = {
        i + j * 1j: c
        for i, r in enumerate(open(input))
        for j, c in enumerate(r.strip())
    }

    start = min(p for p in G if G[p] == "^")

    def walk(G):
        pos, dir, seen = start, -1, set()
        while pos in G and (pos, dir) not in seen:
            seen |= {(pos, dir)}
            if G.get(pos + dir) == "#":
                dir *= -1j
            else:
                pos += dir
        return {p for p, _ in seen}, (pos, dir) in seen

    path = walk(G)[0]

    part_1 = len(path)
    part_2 = sum(walk(G | {o: "#"})[1] for o in path if o != start)

    return part_1, part_2


print(
    f"The solution to part 1 is: {get_solution(input)[0]} \nThe solution to part 2 is: {get_solution(input)[1]}"
)
