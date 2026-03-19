from collections import deque

def reverse_queue(q):
    stack = []

    # Step 1: Dequeue all elements from the queue and push them onto the stack
    while q:
        stack.append(q.popleft())

    # Step 2: Pop all elements from the stack and enqueue them back into the queue
    while stack:
        q.append(stack.pop())

    return q

q = deque([10, 20, 30, 40, 50])
reverse_queue(q)
print("Reversed Queue:", list(q))  # Output: [50, 40, 30, 20, 10]