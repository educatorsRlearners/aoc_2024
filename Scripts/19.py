# Solution minimally adapted from: https://www.reddit.com/r/adventofcode/comments/1hhlb8g/comment/m2s6gnj/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
import re

from functools import cache

sample_input = "data/19_sample.txt"

input = "data/19_data.txt"

# Read the file and process the content
with open(input) as file:
    content = file.read()

lines = [section.splitlines() for section in content.split("\n\n")]

patterns, designs = lines[0][0].split(", "), lines[1]

r = "(" + "|".join(patterns) + ")*"  # star operator to match 0 or more occurences


@cache
def get_count(design):
    if design == "":
        return 1
    # Recursive case: sum the counts for each pattern that matches the start of the design
    count = 0
    for pattern in patterns:
        if design.startswith(pattern):
            count += get_count(design[len(pattern) :])
    return count


total_possible_designs = 0
total_combinations = 0

for design in designs:
    total_possible_designs += re.fullmatch(r, design) != None
    total_combinations += get_count(design)

print(f"Solution for part 1: {total_possible_designs}")
print(f"Solution for part 2: {total_combinations}")
