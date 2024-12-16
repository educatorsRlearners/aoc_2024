from re import findall
from statistics import variance

fn = "data/14_data.txt"

data = open(fn).read()
W, H = 101, 103

robots = []

lines = data.split("\n")

for item in lines:
    matches = findall(r"(-?\d+)", item)
    line_numbers = []

    # Iterate over each match
    for n in matches:
        line_numbers.append(int(n))

    robots.append(line_numbers)

robots

def simulate(t):

    new_location = []

    # Iterate over each tuple (sx, sy, vx, vy) in the robots list
    for sx, sy, vx, vy in robots:
        # Calculate the new positions
        new_x = (sx + t * vx) % W
        new_y = (sy + t * vy) % H

        # Append the new position as a tuple
        new_location.append((new_x, new_y))

    return new_location


bx, bxvar, by, byvar = 0, 10 * 100, 0, 10 * 1000

for t in range(max(W, H)):
    xs, ys = zip(*simulate(t))
    if (xvar := variance(xs)) < bxvar:
        bx, bxvar = t, xvar
    if (yvar := variance(ys)) < byvar:
        by, byvar = t, yvar


print("Part 2:", bx + ((pow(W, -1, H) * (by - bx)) % H) * W)
