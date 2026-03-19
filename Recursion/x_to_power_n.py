def power(x, n):
    # Base case
    if n == 0:
        return 1
    # If n is negative
    if n < 0:
        return 1 / power(x, -n)
    # If n is even
    if n % 2 == 0:
        half = power(x, n // 2)
        return half * half
    # If n is odd
    else:
        return x * power(x, n - 1)

# Example usage
x = 2
n = 5
print(f"{x} to the power {n} is {power(x, n)}")