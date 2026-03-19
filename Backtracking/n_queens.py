def solveNQueens(n):
    def backtrack(row, diagonals, anti_diagonals, cols, state):
        if row == n:
            result.append(["".join(r) for r in state])
            return

        for col in range(n):
            curr_diag = row - col
            curr_anti_diag = row + col
            if (col in cols or curr_diag in diagonals or curr_anti_diag in anti_diagonals):
                continue  # Conflict detected, skip this cell

            # Place queen
            cols.add(col)
            diagonals.add(curr_diag)
            anti_diagonals.add(curr_anti_diag)
            state[row][col] = "Q"

            backtrack(row + 1, diagonals, anti_diagonals, cols, state)

            # Backtrack
            cols.remove(col)
            diagonals.remove(curr_diag)
            anti_diagonals.remove(curr_anti_diag)
            state[row][col] = "."

    result = []
    empty_board = [["."] * n for _ in range(n)]
    backtrack(0, set(), set(), set(), empty_board)
    return result

# Example: Solve 4-Queens
solutions = solveNQueens(4)
for board in solutions:
    for row in board:
        print(row)
    print()