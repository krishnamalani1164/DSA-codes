def update_ith_bit(num, i, bit):
    bit = bit & 1  # Ensure it's either 0 or 1
    return (num & ~(1 << i)) | (bit << i)

# Test case
num = 13        # Binary: 1101
i = 1
bit = 1         # Set bit at position 1 to 1

new_num = update_ith_bit(num, i, bit)
print(f"Original: {bin(num)} ({num})")
print(f"Updated bit {i} to {bit}: {bin(new_num)} ({new_num})")
