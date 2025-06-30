def last_occurrence(arr, x, index=0):
    if index == len(arr):
        return -1
    rest_index = last_occurrence(arr, x, index + 1)
    if rest_index != -1:
        return rest_index
    if arr[index] == x:
        return index
    return -1

# Example usage:
arr = [5, 3, 7, 3, 9]
x = 3
print("Last occurrence of", x, "is at index", last_occurrence(arr, x))
