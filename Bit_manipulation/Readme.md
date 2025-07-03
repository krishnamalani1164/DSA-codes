# Bit Manipulation in Python

## Table of Contents
- [Introduction](#introduction)
- [Binary Number System](#binary-number-system)
- [Bitwise Operators](#bitwise-operators)
- [Common Bit Manipulation Techniques](#common-bit-manipulation-techniques)
- [Practical Applications](#practical-applications)
- [Advanced Techniques](#advanced-techniques)
- [Time and Space Complexity](#time-and-space-complexity)
- [Common Interview Problems](#common-interview-problems)

## Introduction

Bit manipulation is a powerful programming technique that directly operates on binary representations of numbers. It's fundamental to computer science and offers efficient solutions for various computational problems. This README covers essential concepts and practical implementations.

## Binary Number System

### Understanding Binary
- **Binary**: Base-2 number system using only 0s and 1s
- **Bit**: Short for "binary digit" - the smallest unit of data (0 or 1)
- **Byte**: 8 bits grouped together
- **Most Significant Bit (MSB)**: Leftmost bit
- **Least Significant Bit (LSB)**: Rightmost bit

### Binary Representation Examples
```
Decimal 5  → Binary 0101
Decimal 13 → Binary 1101
Decimal 29 → Binary 11101
```

### Two's Complement (Negative Numbers)
In most systems, negative numbers are represented using two's complement:
- Flip all bits and add 1
- Example: -5 in 8-bit = ~(0101) + 1 = 1010 + 1 = 1011

## Bitwise Operators

### 1. AND (&)
- Returns 1 only when both bits are 1
- **Use cases**: Masking, checking specific bits, clearing bits
```
0101 & 0011 = 0001
```

### 2. OR (|)
- Returns 1 when at least one bit is 1
- **Use cases**: Setting bits, combining flags
```
0101 | 0011 = 0111
```

### 3. XOR (^)
- Returns 1 when bits are different
- **Use cases**: Toggling bits, finding unique elements, swapping
```
0101 ^ 0011 = 0110
```

### 4. NOT (~)
- Flips all bits (1's complement)
- **Use cases**: Creating masks, bit inversion
```
~0101 = 1010 (in relevant bit width)
```

### 5. Left Shift (<<)
- Shifts bits to the left, filling with zeros
- **Equivalent to**: Multiplying by 2^n
```
0101 << 1 = 1010 (5 * 2 = 10)
```

### 6. Right Shift (>>)
- Shifts bits to the right
- **Equivalent to**: Integer division by 2^n
```
0101 >> 1 = 0010 (5 / 2 = 2)
```

## Common Bit Manipulation Techniques

### 1. Check if Number is Even or Odd
```python
def is_even(n):
    return (n & 1) == 0
```
**Logic**: LSB is 0 for even numbers, 1 for odd numbers

### 2. Get i-th Bit
```python
def get_bit(num, i):
    return (num >> i) & 1
```
**Logic**: Shift right to bring i-th bit to LSB position, then mask with 1

### 3. Set i-th Bit
```python
def set_bit(num, i):
    return num | (1 << i)
```
**Logic**: Create mask with 1 at i-th position, OR with number

### 4. Clear i-th Bit
```python
def clear_bit(num, i):
    return num & ~(1 << i)
```
**Logic**: Create mask with 0 at i-th position, AND with number

### 5. Update i-th Bit
```python
def update_bit(num, i, bit_value):
    return (num & ~(1 << i)) | (bit_value << i)
```
**Logic**: Clear the bit first, then set it to desired value

### 6. Check if Power of 2
```python
def is_power_of_2(n):
    return n > 0 and (n & (n - 1)) == 0
```
**Logic**: Powers of 2 have only one bit set. `n & (n-1)` removes the lowest set bit

### 7. Count Set Bits (Population Count)
```python
def count_set_bits(n):
    count = 0
    while n:
        n = n & (n - 1)  # Remove lowest set bit
        count += 1
    return count
```
**Logic**: Brian Kernighan's algorithm - each operation removes one set bit

### 8. Clear Last i Bits
```python
def clear_last_i_bits(num, i):
    return num & (~((1 << i) - 1))
```
**Logic**: Create mask with i trailing zeros, AND with number

## Practical Applications

### 1. Fast Exponentiation
```python
def fast_power(base, exp):
    result = 1
    while exp > 0:
        if exp & 1:  # If exp is odd
            result *= base
        base *= base
        exp >>= 1    # Divide exp by 2
    return result
```

### 2. Finding Unique Element
When all elements appear twice except one:
```python
def find_unique(arr):
    result = 0
    for num in arr:
        result ^= num
    return result
```

### 3. Swapping Without Temporary Variable
```python
def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b
```

### 4. Checking if Two Numbers Have Opposite Signs
```python
def opposite_signs(a, b):
    return (a ^ b) < 0
```

## Advanced Techniques

### 1. Isolate Rightmost Set Bit
```python
def isolate_rightmost_set_bit(n):
    return n & (-n)
```

### 2. Turn Off Rightmost Set Bit
```python
def turn_off_rightmost_set_bit(n):
    return n & (n - 1)
```

### 3. Check if Number is a Power of 4
```python
def is_power_of_4(n):
    return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0
```

### 4. Reverse Bits
```python
def reverse_bits(n):
    result = 0
    for _ in range(32):  # Assuming 32-bit integer
        result = (result << 1) | (n & 1)
        n >>= 1
    return result
```

## Time and Space Complexity

### Advantages of Bit Manipulation:
- **Time Complexity**: Most operations are O(1)
- **Space Complexity**: O(1) - no extra space needed
- **Performance**: Directly maps to processor instructions
- **Memory Efficient**: Can pack multiple boolean values into single integer

### When to Use:
- Performance-critical applications
- Memory-constrained environments
- Mathematical computations
- Cryptography and hashing
- Graphics programming
- Embedded systems

## Common Interview Problems

### 1. Missing Number
Find the missing number in array containing n distinct numbers from 0 to n.

### 2. Single Number
Find the number that appears once in array where every other number appears twice.

### 3. Power of Two
Determine if given integer is a power of two.

### 4. Number of 1 Bits
Count the number of set bits in integer.

### 5. Reverse Integer
Reverse the bits of a 32-bit unsigned integer.

### 6. Maximum XOR
Find two numbers in array such that their XOR is maximum.

## Best Practices

1. **Understand the Problem**: Identify if bit manipulation can provide an efficient solution
2. **Use Meaningful Names**: Make bit operations readable with descriptive function names
3. **Comment Complex Operations**: Explain the logic behind non-obvious bit manipulations
4. **Test Edge Cases**: Include tests for 0, negative numbers, and boundary values
5. **Consider Bit Width**: Be aware of integer size limitations in your language
6. **Use Built-in Functions**: When available, use optimized library functions like `popcount`

## Conclusion

Bit manipulation is a fundamental skill that can significantly optimize your code. While it may seem complex initially, mastering these techniques will make you a more efficient programmer and help you solve complex problems elegantly. Practice these patterns, understand the underlying logic, and you'll find bit manipulation becomes an intuitive tool in your programming toolkit.

Remember: The key to mastering bit manipulation is understanding binary representation and practicing common patterns until they become second nature.
