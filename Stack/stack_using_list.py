class Stack:
    def __init__(self):
        self.stack=[]
    
    def push(self,item):
        #Add an item to the top of the stack
        self.stack.append(item)
    
    def pop(self):
        #Remove and return the top item from the stack
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Pop from an empty stack")

    def peek(self):
        #Return the top item from the stack without removing it
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Peek from an empty stack")
    
    def is_empty(self):
        #Check if the stack is empty
        return len(self.stack)==0
    
    def size(self):
        #Return the number of items in the stack
        return len(self.stack)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Top of stack:",stack.peek())
print("Size of stack:",stack.size())
print("Popped:",stack.pop())
print("Stack size after pop:",stack.size())