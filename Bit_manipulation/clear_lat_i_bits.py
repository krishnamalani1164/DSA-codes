def clear_last_i_bits(num, i):
    return num & (~((1 << i) - 1))

# Test case
num = 29   # Binary: 11101
i = 3      # Clear last 3 bits
new_num = clear_last_i_bits(num, i)
print(f"Original: {bin(num)} ({num})")
print(f"After clearing last {i} bits: {bin(new_num)} ({new_num})")
