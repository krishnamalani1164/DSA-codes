def staircase_search(matrix, target):
    if not matrix or not matrix[0]:
        return False

    rows = len(matrix)
    cols = len(matrix[0])
    
    row = 0
    col = cols - 1  # Start at top-right corner

    while row < rows and col >= 0:
        current = matrix[row][col]
        if current == target:
            return True
        elif current > target:
            col -= 1  # Move left
        else:
            row += 1  # Move down

    return False

matrix = [
    [1,  4,  7, 11],
    [2,  5,  8, 12],
    [3,  6,  9, 16],
    [10, 13, 14, 17]
]
target = 9

print(staircase_search(matrix, target))  # Output: True
