def permute(s, l, r):
    if l == r:
        print("".join(s))
    else:
        for i in range(l, r + 1):
            s[l], s[i] = s[i], s[l]         # Swap
            permute(s, l + 1, r)            # Recurse
            s[l], s[i] = s[i], s[l]         # Backtrack

# Initial call
string = "abc"
permute(list(string), 0, len(string) - 1)