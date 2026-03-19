def max_chain_length(pairs):
    # Step 1: Sort pairs based on the second value
    pairs.sort(key=lambda x: x[1])

    # Step 2: Greedy selection
    current_end = float('-inf')
    chain_length = 0

    for pair in pairs:
        if pair[0] > current_end:
            chain_length += 1
            current_end = pair[1]

    return chain_length


# Example usage
pairs = [[5, 24], [15, 25], [27, 40], [50, 60]]
print("Maximum length of chain:", max_chain_length(pairs))
