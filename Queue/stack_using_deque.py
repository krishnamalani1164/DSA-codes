from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, val):
        self.stack.append(val)  # Push to top

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()  # Pop from top

    def peek(self):
        return self.stack[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

s = Stack()
s.push(10)
s.push(20)
s.push(30)

print(s.pop())   # Output: 30
print(s.peek())  # Output: 20
print(s.size())  # Output: 2
