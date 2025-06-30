def friends_pairing(n):
    # Base cases
    if n == 0 or n == 1:
        return 1
    # Recursive case
    return friends_pairing(n - 1) + (n - 1) * friends_pairing(n - 2)

# Example usage
n = 4
print(f"Number of ways {n} friends can pair up or stay single: {friends_pairing(n)}")