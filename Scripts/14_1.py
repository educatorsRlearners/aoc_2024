from re import findall
from collections import defaultdict

fn = "data/14_data.txt"

data = open(fn).read()
w, h = 101, 103

robots = []

lines = data.split("\n")

for item in lines:
    matches = findall(r"(-?\d+)", item)
    line_numbers = []

    # Iterate over each match
    for n in matches:
        line_numbers.append(int(n))

    robots.append(line_numbers)


def advance(r):
    (x, y), (vx, vy) = r
    x += vx
    y += vy

    # Handle wrapping around the width and height
    while x < 0:
        x += w
    while x >= w:
        x -= w
    while y < 0:
        y += h
    while y >= h:
        y -= h

    return (x, y), (vx, vy)

# Advance each robot
for i in range(len(robots)):
    robots[i] = advance(robots[i])

print(robots)
