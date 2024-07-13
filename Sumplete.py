import numpy as np

def solve_sumplete(grid, row_sums, col_sums):
    nrows, ncols = grid.shape
    solution = np.zeros_like(grid)
    memo = {}

    def is_valid_partial(solution, row_sums, col_sums, row, col):
        current_row_sums = solution.sum(axis=1)
        current_col_sums = solution.sum(axis=0)
        if current_row_sums[row] > row_sums[row] or current_col_sums[col] > col_sums[col]:
            return False
        return True

    def backtrack(row, col):
        if row == nrows:
            return np.all(solution.sum(axis=1) == row_sums) and np.all(solution.sum(axis=0) == col_sums)

        state = (row, col, tuple(solution.flatten()))
        if state in memo:
            return memo[state]

        next_row, next_col = (row, col + 1) if col + 1 < ncols else (row + 1, 0)

        # Try excluding the current cell first (greedy approach)
        solution[row, col] = 0
        if is_valid_partial(solution, row_sums, col_sums, row, col) and backtrack(next_row, next_col):
            memo[state] = True
            return True

        # Try including the current cell
        solution[row, col] = grid[row, col]
        if is_valid_partial(solution, row_sums, col_sums, row, col) and backtrack(next_row, next_col):
            memo[state] = True
            return True

        # Backtrack
        solution[row, col] = 0
        memo[state] = False
        return False

    if backtrack(0, 0):
        return solution.tolist()
    else:
        return None

def main():
    nrows = int(input("Enter the number of rows: "))
    ncols = int(input("Enter the number of columns: "))

    print("Enter the grid values row by row (space-separated):")
    number_grid = []
    for _ in range(nrows):
        row = list(map(int, input().split()))
        number_grid.append(row)

    print("Enter the row sums (space-separated):")
    row_sums = list(map(int, input().split()))

    print("Enter the column sums (space-separated):")
    col_sums = list(map(int, input().split()))

    grid = np.array(number_grid)
    solution = solve_sumplete(grid, row_sums, col_sums)

    if solution is not None:
        print("Solution found:")
        for row in solution:
            print(row)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
