def min_abs_diff_pair(A, B):
    A.sort()
    B.sort()
    
    i = j = 0
    min_diff = float('inf')
    pair = ()

    while i < len(A) and j < len(B):
        diff = abs(A[i] - B[j])
        if diff < min_diff:
            min_diff = diff
            pair = (A[i], B[j])

        # Move pointer in the direction of smaller element
        if A[i] < B[j]:
            i += 1
        else:
            j += 1

    return pair, min_diff


# Example usage
A = [1, 3, 15, 11, 2]
B = [23, 127, 235, 19, 8]
result = min_abs_diff_pair(A, B)
print("Closest pair:", result[0])
print("Minimum absolute difference:", result[1])
