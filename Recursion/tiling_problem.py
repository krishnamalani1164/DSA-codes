def tiling(n):
    # Base cases
    if n == 0 or n == 1:
        return 1
    # Recursive case
    return tiling(n - 1) + tiling(n - 2)

# Example usage
n = 5
print(f"Number of ways to tile a 2×{n} board: {tiling(n)}")