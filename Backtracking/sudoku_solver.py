def isValid(board, row, col, num):
    num = str(num)
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

        boxRow = 3 * (row // 3) + i // 3
        boxCol = 3 * (col // 3) + i % 3
        if board[boxRow][boxCol] == num:
            return False
    return True

def solveSudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == '.' or board[row][col] == '0':
                for num in range(1, 10):
                    if isValid(board, row, col, num):
                        board[row][col] = str(num)
                        if solveSudoku(board):
                            return True
                        board[row][col] = '.'  # Backtrack
                return False
    return True

# Example input board
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

if solveSudoku(board):
    print("Yes")
else:
    print("No")
