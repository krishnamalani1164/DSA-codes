def fill_array(arr, index, value):
    # Base case: if we've filled the array
    if index == len(arr):
        return

    # Fill current index
    arr[index] = value

    # Recursive call to fill the next index
    fill_array(arr, index + 1, value + 1)

    # Backtracking step: decrement by 2
    arr[index] -= 2

# Initialize array of size 5
arr = [0] * 5
fill_array(arr, 0, 1)
print("Final array after backtracking:", arr)
