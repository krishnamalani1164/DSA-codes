def countWays(i, j, m, n):
    # Base Case: reached bottom-right
    if i == m - 1 and j == n - 1:
        return 1

    # If out of bounds
    if i >= m or j >= n:
        return 0

    # Explore down and right paths
    down = countWays(i + 1, j, m, n)
    right = countWays(i, j + 1, m, n)

    return down + right

# Wrapper function
def gridWays(m, n):
    return countWays(0, 0, m, n)

# Example usage
print(gridWays(3, 3))  # Output: 6
