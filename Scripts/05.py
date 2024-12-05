with open("data/05_data.txt") as f:
    lines = f.read().splitlines()

ordering, updates = [], []

for line in lines:
    if line.__contains__("|"):
        ordering.append(line)
    else:
        updates.append(line)

ordering_list = [list(map(int, ordering.split("|"))) for ordering in ordering]
updates_list = [list(map(int, update.split(","))) for update in updates if update]


def comes_before(element1, element2, ordering_list):
    for ordering in ordering_list:
        if element1 in ordering and element2 in ordering:
            if ordering.index(element1) < ordering.index(element2):
                return True
    return False


def correct_order(updates):
    is_correct_order = True

    for i in range(len(updates) - 1):
        if not comes_before(updates[i], updates[i + 1], ordering_list):
            is_correct_order = False
            break

    return is_correct_order


keepers = []
incorrect_order = []

for update in updates_list:
    if correct_order(update):
        keepers.append(update)
    else:
        incorrect_order.append(update)


def get_middle_element(lst):
    middle_index = len(lst) // 2
    return lst[middle_index]


get_part_1 = sum([get_middle_element(keeper) for keeper in keepers])


if __name__ == "__main__":
    print(get_part_1)
