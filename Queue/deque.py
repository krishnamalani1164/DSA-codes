from collections import deque

# Create a deque
dq = deque()

# Insert elements
dq.append(10)       # add to rear
dq.appendleft(5)    # add to front

print(dq)  # deque([5, 10])

# Remove elements
dq.pop()            # removes from rear → 10
dq.popleft()        # removes from front → 5