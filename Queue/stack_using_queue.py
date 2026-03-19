from queue import Queue

class StackUsingQueues:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self,item):
        #Copy contents of queue1 to queue2
        while not self.queue1.empty():
            self.queue2.put(self.queue1.get())

        #Add new element  to queue1
        self.queue1.put(item)

        #Copy contents of queue2 back to queue1
        while not self.queue2.empty():
            self.queue1.put(self.queue2.get())

    def pop(self):
        if self.queue1.empty():
            return None
        return self.queue1.get()
        
    def top(self):
        if self.queue1.empty():
            return None
        return self.queue1.queue[0]
        
    def is_empty(self):
        return self.queue1.empty()

# Example usage
stack = StackUsingQueues()
stack.push(10)
stack.push(20)
print(stack.pop())  # Output: 20
print(stack.top())  # Output: 10
print(stack.is_empty())  # Output: False