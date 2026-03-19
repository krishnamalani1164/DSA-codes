def is_power_of_2(num):
    return num > 0 and (num & (num - 1)) == 0

# Test cases
for n in [1, 2, 3, 4, 8, 10, 16, 18, 32, 0, -8]:
    print(f"{n}: {'Power of 2' if is_power_of_2(n) else 'Not a power of 2'}")
