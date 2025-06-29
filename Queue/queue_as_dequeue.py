from collections import deque

class Queue:
    def __init__(self):
        self.q = deque()

    def enqueue(self, val):
        self.q.append(val)  # add to rear

    def dequeue(self):
        if self.is_empty():
            return None
        return self.q.popleft()  # remove from front

    def peek(self):
        return self.q[0] if not self.is_empty() else None

    def is_empty(self):
        return len(self.q) == 0

    def size(self):
        return len(self.q)
    
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())  # Output: 10
print(q.peek())     # Output: 20
print(q.size())     # Output: 2