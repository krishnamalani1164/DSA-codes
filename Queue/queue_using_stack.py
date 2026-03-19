class QueueUsingTwoStacks:
    # Constructor for simulation of queue using two stacks
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        # Push all elements from stack1 to stack2
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        # Push element x to stack1
        self.stack1.append(x)

        # Push everything back to stack1 from stack2
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self):
        # Pop the element from stack1
        if not self.stack1:
            return None
        return self.stack1.pop()

    def front(self):
        # Return the front element from stack1
        if not self.stack1:
            return None
        return self.stack1[-1]  # Returning last element of the stack
    
    def empty(self):
        # Return true if stack1 is empty, false otherwise
        return len(self.stack1) == 0

# Example usage:
queue = QueueUsingTwoStacks()
queue.push(1)
queue.push(2)
queue.push(3)
print(queue.front())  # Output: 1
print(queue.pop())    # Output: 1
print(queue.front())  # Output: 2
print(queue.pop())    # Output: 2
print(queue.front())  # Output: 3
print(queue.pop())    # Output: 3
print(queue.empty())  # Output: True