# Made with perplexity

with open("data/04_data.txt") as f:
    grid = f.read().splitlines()


def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),  # horizontal and vertical
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),  # diagonal
    ]

    def check_xmas(row, col, dr, dc):
        if 0 <= row < rows and 0 <= col < cols and grid[row][col] == "X":
            if (
                0 <= row + dr < rows
                and 0 <= col + dc < cols
                and grid[row + dr][col + dc] == "M"
                and 0 <= row + 2 * dr < rows
                and 0 <= col + 2 * dc < cols
                and grid[row + 2 * dr][col + 2 * dc] == "A"
                and 0 <= row + 3 * dr < rows
                and 0 <= col + 3 * dc < cols
                and grid[row + 3 * dr][col + 3 * dc] == "S"
            ):
                return True
        return False

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if check_xmas(r, c, dr, dc):
                    count += 1

    return count


def count_x_mas_pt2(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def check_x_mas(r, c):
        if r + 2 >= rows or c - 1 < 0 or c + 1 >= cols:
            return False

        center = grid[r + 1][c]
        if center != "A":
            return False

        top_left = grid[r][c - 1]
        top_right = grid[r][c + 1]
        bottom_left = grid[r + 2][c - 1]
        bottom_right = grid[r + 2][c + 1]

        return (
            (
                top_left in "MS"
                and top_right in "MS"
                and bottom_left in "MS"
                and bottom_right in "MS"
            )
            and (
                (top_left == "M" and bottom_right == "S")
                or (top_left == "S" and bottom_right == "M")
            )
            and (
                (top_right == "M" and bottom_left == "S")
                or (top_right == "S" and bottom_left == "M")
            )
        )

    for r in range(rows - 2):
        for c in range(1, cols - 1):
            if check_x_mas(r, c):
                count += 1

    return count


if __name__ == "__main__":
    print(count_xmas(grid))
    print(count_x_mas_pt2(grid))
