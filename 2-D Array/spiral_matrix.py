def generate_spiral_matrix(n):
    # Create an empty n x n matrix
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    # Initialize boundaries
    top = 0
    bottom = n - 1
    left = 0
    right = n - 1

    num = 1  # Start filling from 1

    while top <= bottom and left <= right:
        # ➡️ Traverse from left to right
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        # ⬇️ Traverse from top to bottom
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # ⬅️ Traverse from right to left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

        # ⬆️ Traverse from bottom to top
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

    return matrix
n = 4
spiral = generate_spiral_matrix(n)

# Print the matrix
for row in spiral:
    print(row)
