import numpy as np


with open("data/02_data.txt", "r") as file:
    lines = [line.strip().split(" ") for line in file]


def check_increasing_or_decreasing(df):

    monotonic = np.all(np.diff(df) > 0) | np.all(np.diff(df) < 0)
    filtered_rows = df[monotonic]

    condition_2 = np.all(np.diff(filtered_rows).__abs__() <= 3)
    filtered_rows_2 = filtered_rows[condition_2]

    return filtered_rows_2


total = 0

for line in lines:
    test = np.array(line, dtype=int)
    if check_increasing_or_decreasing(test).size > 0:
        total += 1

print("Solution for part 1:", total)
