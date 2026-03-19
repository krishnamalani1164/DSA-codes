def remove_duplicates(s, index=0, seen=set(), result=""):
    # Base case: if we've reached the end of the string
    if index == len(s):
        return result

    current_char = s[index]

    # If character hasn't been seen, add it to result and mark as seen
    if current_char not in seen:
        seen.add(current_char)
        result += current_char

    # Recurse for the next character
    return remove_duplicates(s, index + 1, seen, result)

# Example usage
input_str = "aabbccddeeff"
print("Original:", input_str)
print("Without duplicates:", remove_duplicates(input_str))