def diagonal_sum(matrix):
    n = len(matrix)
    total = 0

    for i in range(n):
        total += matrix[i][i]                     # Primary diagonal
        total += matrix[i][n - 1 - i]             # Secondary diagonal

    # If n is odd, subtract the center element (it's added twice)
    if n % 2 == 1:
        total -= matrix[n // 2][n // 2]

    return total

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Diagonal Sum:", diagonal_sum(matrix))
