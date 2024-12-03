import re


def get_results(corrupted_data):
    pattern = r"mul\(\d+,\d+\)"
    matches = re.findall(pattern, corrupted_data)

    numbers = []

    for match in matches:
        nums = re.findall(r"\d+", match)
        numbers.append(int(nums[0]) * int(nums[1]))

    return sum(numbers)


all_results = []

with open("data/03_data.txt", "r") as file:
    for line in file:
        all_results.append(get_results(line))

print("The solution to part 1 is:", sum(all_results))
