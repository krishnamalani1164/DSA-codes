from collections import deque

def first_non_repeating(stream):
    freq = {}
    q = deque()

    for ch in stream:
        # Simple loop to increment frequency
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

        q.append(ch)

        # Remove characters from the front that are no longer non-repeating
        while q and freq[q[0]] > 1:
            q.popleft()

        # Display the result
        if q:
            print(f"First non-repeating: {q[0]}")
        else:
            print("No non-repeating character")

first_non_repeating("aabcbd")