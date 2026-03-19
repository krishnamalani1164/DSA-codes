a = 5   # Binary: 0101
b = 3   # Binary: 0011

print("a =", a, "->", bin(a))
print("b =", b, "->", bin(b))

# Bitwise AND
print("a & b =", a & b)   # 0101 & 0011 = 0001 -> 1

# Bitwise OR
print("a | b =", a | b)   # 0101 | 0011 = 0111 -> 7

# Bitwise XOR
print("a ^ b =", a ^ b)   # 0101 ^ 0011 = 0110 -> 6

# Bitwise NOT
print("~a =", ~a)         # ~0101 = -(a + 1) = -6

# Left Shift
print("a << 1 =", a << 1) # 0101 << 1 = 1010 -> 10

# Right Shift
print("a >> 1 =", a >> 1) # 0101 >> 1 = 0010 -> 2
