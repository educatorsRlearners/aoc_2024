import os
from collections import Counter

INPUT_PATH = "data/11_data.txt"

demo_data = [125, 17]


with open(INPUT_PATH) as file:
    data = list(map(int, file.read().strip().split()))


def solve(numbers, steps):
    counter = Counter(numbers)
    for step in range(steps):
        step_counter = Counter()
        for n, count in counter.items():
            str_n = str(n)
            if n == 0:
                step_counter[1] += count
            elif len(str_n) % 2 == 0:
                middle = len(str_n) // 2
                step_counter[int(str_n[:middle])] += count
                step_counter[int(str_n[middle:])] += count
            else:
                step_counter[n * 2024] += count
        counter = step_counter

    return counter.total()


demo_res = solve(demo_data, 25)
assert demo_res == 55312, demo_res

res = solve(data, 25)
res_2 = solve(data, 75)

print(f"The solution to part 1 is: {res}")
print(f"The solution to part 2 is: {res_2}")
