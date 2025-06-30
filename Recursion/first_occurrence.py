def first_occurrence(arr, x, index=0):
    if index == len(arr):
        return -1
    if arr[index] == x:
        return index
    return first_occurrence(arr, x, index + 1)

# Example usage:
arr = [5, 3, 7, 3, 9]
x = 3
print("First occurrence of", x, "is at index", first_occurrence(arr, x))
