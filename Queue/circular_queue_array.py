class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1
    
    def enqueue(self, value):
        if (self.rear + 1) % self.size == self.front:
            print("Circular Queue is full")
        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value

    def dequeue(self):
        if self.front == -1:
            print("Circular Queue is empty")
            return None
        result = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return result

    def display(self):
        if self.front == -1:
            print("No element in the Circular Queue")
        else:
            i = self.front
            queue_elements = []
            while i != self.rear:
                queue_elements.append(self.queue[i])
                i = (i + 1) % self.size
            queue_elements.append(self.queue[self.rear])
            print("Circular Queue elements:", queue_elements)

# Example usage
q = CircularQueue(5)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.display()
print("Dequeued:", q.dequeue())
q.display()
q.enqueue(6)
q.display()
