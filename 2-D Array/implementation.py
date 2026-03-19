# Creating a 2D array of size 3x3 filled with zeros
rows, cols = 3, 3
arr = [[0 for _ in range(cols)] for _ in range(rows)]

# Example: Populating the array with row * col values
for i in range(rows):
    for j in range(cols):
        arr[i][j] = (i + 1) * (j + 1)

# Printing the 2D array in matrix format
print("2D Array:")
for row in arr:
    for value in row:
        print(value, end=' ')
    print()

# Accessing and modifying a specific element
print("\nOriginal element at [1][2]:", arr[1][2])
arr[1][2] = 99
print("Modified element at [1][2]:", arr[1][2])

# Final 2D Array
print("\nFinal 2D Array:")
for row in arr:
    print(row)
