def set_ith_bit(num, i):
    return num | (1 << i)

# Test case
num = 9       # Binary: 1001
i = 1         # Set bit at index 1 (from LSB)
new_num = set_ith_bit(num, i)
print(f"Original: {bin(num)} ({num})")
print(f"After setting bit {i}: {bin(new_num)} ({new_num})")