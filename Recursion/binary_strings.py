def generate_binary_strings(n, last_digit=0, current=""):
    # Base case: if the string is of length n, print it
    if n == 0:
        print(current)
        return

    # Always allowed to add '0'
    generate_binary_strings(n - 1, 0, current + "0")

    # Only add '1' if the last digit was not '1'
    if last_digit == 0:
        generate_binary_strings(n - 1, 1, current + "1")

# Example usage
n = 3
print(f"Binary strings of length {n} with no consecutive 1s:")
generate_binary_strings(n)