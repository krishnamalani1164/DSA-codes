def clear_ith_bit(num, i):
    return num & ~(1 << i)

# Test case
num = 15      # Binary: 1111
i = 2         # Clear bit at index 2 (from LSB)
new_num = clear_ith_bit(num, i)
print(f"Original: {bin(num)} ({num})")
print(f"After clearing bit {i}: {bin(new_num)} ({new_num})")