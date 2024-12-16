# Explanation: https://www.reddit.com/r/adventofcode/comments/1hfboft/comment/m2bae5n/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
# Code: https://topaz.github.io/paste/#XQAAAQDCCgAAAAAAAAA0m0pnuFI8c9q4WY2st6n38pCwBkXijbbjhcCL/t4DIOf5X/27/bV/PA/rSSPegEvg85OIisN7tgXLLx2nrxizpRyfuBY0YTFaF0te1rIFV3QwuFTCBJagKdsbatJAoZYsfxpzvyDkCvQv4UmQIUBycxakCP+JminESFBdpQgrWvjHSTO+wy+8CTFBQH5G7ClqJjGhbAQWCLnujErhY5yRpS+PrHp40e1fuBsLi+Xs0Tnlg0Gmu4Fpqr6159NbzX7gX4hh8TFqPJ9WvxayIDjYtUAMi6Tu3rVpUj+ZMEat9eY54uMO88wwnabuAU5rluvjjGP1cI9oNfdPC3ojm0jb2Qu8lmiIqFY5jCE5/D6ckUy2GXHYOPweoFHaVK/kVY+sKfV/O7+c8c0/TKUOnh8odrmB0JSAqt1XVJqLbIf2ctLwapqsWVlVZNdMjQbVLsKF2iPh+YpCEcPI8N8JpqUGYjrJbejSwrgjlfgZw5rULBaRw+rlwkXCklPi2enwggzVH47o4AecDdQQoGnnBMt8U98t6+0O+byz+004BDmOduDvCrTfzO5rFUgAgS5oJzH4spgU4mHJC2tIppm3xgiRnKTc7/6Sz2s7vSjQc1apX0pg9tesOvRZjznSP0uKKehTzTEdWQX4ZFKQsLP6upBHXgeWPcRsCrwi1M1ai945s1PspfetEn9pBLvpxlJP9np9C72FgvEApWl/bhtDCaa0eOYb59duuQHBxunaFJV4ANnq2SikKgtxX1sMJYKoPb1mung10X6uti4x5cFIvvDYKESkUOEExeT51+Dez9EX+GV25up6QkqJ7k7tUHbsoIMA1eI3N+9vZKsZaxGUZfAr7R/dFvuLis79kEPTzrM5cAUzicxn7Lxd583I5ZD3XMT1HAox3UR/W9o3/ISRBnHARVJNfZPmi3sjQFpKGIjlHTbtKQ2mrUlRmwqQ22KRPtHbjtMS/yAkK2zcuKLBWmBeHenyPfTjLkNC/PbzvMExwvVpACPg5TPC7eanlPVflVGak0lPveaLyXUkbK1vxHEn/L9mLUEVxIKDs8YDGmxn+jAMQD7EfQAwi0nFO37v31M0FY8Ze6E4DpvnfqgmbbI7aUZ6a636oOOSZg3zxuo4hAIzF1AdbBLofN+pw2XKhhQHykhzLkFSN5X/5z2zJA==

import heapq


def parse(lines):
    grid = []
    line = 0
    for line in range(len(lines)):
        grid.append(list(lines[line].strip()))

    s = None
    e = None
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == "S":
                s = (r, c)
            elif ch == "E":
                e = (r, c)
    return grid, s, e


def dijkstra(grid, starts):
    delta = {"E": (0, 1), "W": (0, -1), "N": (-1, 0), "S": (1, 0)}

    dist = {}
    pq = []
    for sr, sc, dir in starts:
        dist[(sr, sc, dir)] = 0
        heapq.heappush(pq, (0, sr, sc, dir))

    while pq:
        (d, row, col, direction) = heapq.heappop(pq)
        if dist[(row, col, direction)] < d:
            continue
        for next_dir in "EWNS".replace(direction, ""):
            if (row, col, next_dir) not in dist or dist[
                (row, col, next_dir)
            ] > d + 1000:
                dist[(row, col, next_dir)] = d + 1000
                heapq.heappush(pq, (d + 1000, row, col, next_dir))
        dr, dc = delta[direction]
        next_row, next_col = row + dr, col + dc
        if (
            0 <= next_row < len(grid)
            and 0 <= next_col < len(grid[0])
            and grid[next_row][next_col] != "#"
            and (
                (next_row, next_col, direction) not in dist
                or dist[(next_row, next_col, direction)] > d + 1
            )
        ):
            dist[(next_row, next_col, direction)] = d + 1
            heapq.heappush(pq, (d + 1, next_row, next_col, direction))

    return dist


def part1(input):
    grid, (sr, sc), (er, ec) = input
    dist = dijkstra(grid, [(sr, sc, "E")])
    best = 1000000000
    for dir in "EWNS":
        if (er, ec, dir) in dist:
            best = min(best, dist[(er, ec, dir)])
    return best


def part2(input):
    grid, (sr, sc), (er, ec) = input
    from_start = dijkstra(grid, [(sr, sc, "E")])
    from_end = dijkstra(grid, [(er, ec, d) for d in "EWNS"])
    optimal = part1(input)
    flip = {"E": "W", "W": "E", "N": "S", "S": "N"}
    result = set()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            for dir in "EWNS":
                state_from_start = (row, col, dir)
                state_from_end = (row, col, flip[dir])
                if state_from_start in from_start and state_from_end in from_end:
                    if (
                        from_start[state_from_start] + from_end[state_from_end]
                        == optimal
                    ):
                        result.add((row, col))
    return len(result)


input_file = "data/16_data.txt"

input = parse(open(input_file).readlines())


print(part1(input))
print(part2(input))
