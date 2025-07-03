def count_set_bits(num):
    count = 0
    while num:
        num = num & (num - 1)  # clears the lowest set bit
        count += 1
    return count

num = 29  # Binary: 11101 → 4 set bits

print("Using bin():", bin(num).count('1'))
print("Using bitwise method:", count_set_bits(num))
