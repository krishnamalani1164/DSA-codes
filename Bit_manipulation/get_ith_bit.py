def get_ith_bit(num, i):
    return (num >> i) & 1

# Test case
num = 13  # Binary: 1101
for i in range(4):
    print(f"Bit at position {i} (from LSB):", get_ith_bit(num, i))
