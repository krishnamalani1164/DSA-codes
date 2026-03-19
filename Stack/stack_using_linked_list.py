class Node:
    def __init__(self, data):
        self.data = data #Store the data of the node
        self.next = None #Reference to the next node in the stack

class Stack:
    def __init__(self):
        self.top = None #Reference to the top node in the stack

    def push(self,data):
        #Add an item to the top of the stack
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        #Remove an item from the top of the stack
        if  self.is_empty():
            raise IndexError("Pop from an empty stack")
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data
    
    def peek(self):
        #Return the top item without removing it
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.top.data

    def is_empty(self):
        return self.top is None
    
    def size(self):
        #Return the number of items in the stack
        current = self.top
        count = 0
        while current:
            count += 1
            current = current.next
        return count

if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Top Element:",stack.peek())
    print("Size of Stack:",stack.size())
    print("Popped:",stack.pop())
    print("Stack size after pop:",stack.size())
