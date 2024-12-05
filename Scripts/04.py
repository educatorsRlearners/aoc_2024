# Source: https://www.reddit.com/r/adventofcode/comments/1h689qf/comment/m0bsh3p/

# Parse the grid into a dictionary of (y,x):c
data = open("data/04_data.txt").readlines()

# Get the shape of the grid
H, W = len(data), len(data[0]) - 1

# Get the coordinates for every square and the value in that coordinate
grid = {(y, x): data[y][x] for y in range(H) for x in range(W)}

# Part 1 - Find anything that says 'XMAS'
TARGET = "XMAS"

# Define the 8 directions to check
DELTAS = [(dy, dx) for dy in [-1, 0, 1] for dx in [-1, 0, 1] if (dx != 0 or dy != 0)]

count = 0
for y, x in grid:
    for dy, dx in DELTAS:
        candidate = "".join(
            grid.get((y + dy * i, x + dx * i), "") for i in range(len(TARGET))
        )
        count += candidate == TARGET
print("Part 1:", count)

# Part 2 - Find an MAS 'X'...
count = 0
for y, x in grid:
    if grid[y, x] == "A":
        lr = grid.get((y - 1, x - 1), "") + grid.get((y + 1, x + 1), "")
        rl = grid.get((y - 1, x + 1), "") + grid.get((y + 1, x - 1), "")
        count += {lr, rl} <= {"MS", "SM"}
print("Part 2:", count)
