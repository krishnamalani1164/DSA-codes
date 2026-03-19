def find_subsets(s, index=0, current="", result=[]):
    if index == len(s):
        result.append(current)
        return

    # Include the current character
    find_subsets(s, index + 1, current + s[index], result)

    # Exclude the current character
    find_subsets(s, index + 1, current, result)

    return result

# Example usage
s = "abc"
subsets = find_subsets(s)
print("All subsets:", subsets)