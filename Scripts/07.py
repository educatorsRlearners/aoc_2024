from collections import defaultdict

all_data = "data/07_data.txt"

data_dict = defaultdict(list)

with open(all_data, "r") as file:
    for line in file:
        key, values = line.split(":")
        values_list = list(map(int, values.strip().split()))
        data_dict[int(key)] = values_list


def generate_expressions(numbers, index=0, current_value=0):
    if index == len(numbers):
        return [current_value]

    results = []

    if index == 0:
        results += generate_expressions(numbers, index + 1, numbers[index])
    else:
        results += generate_expressions(
            numbers, index + 1, current_value + numbers[index]
        )
        results += generate_expressions(
            numbers, index + 1, current_value * numbers[index]
        )

    return results


def get_part_1(data):
    result = []

    for k, v in data_dict.items():
        if k in generate_expressions(v):
            result.append(k)

    return sum(result)


if __name__ == "__main__":
    print(f" The solution to part 1 is: {get_part_1(data_dict)}")
