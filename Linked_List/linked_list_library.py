from collections import deque

# Create a deque (acts like a doubly-linked list)
ll = deque()

# Insertion
ll.append(10)
ll.append(20)
ll.appendleft(5)

print(ll)  # Output: deque([5, 10, 20])

# Deletion
ll.pop()       # removes 20
ll.popleft()   # removes 5

print(ll)  # Output: deque([10])