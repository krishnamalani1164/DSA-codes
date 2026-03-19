from typing import Generic , TypeVar,List

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self.stack: List[T] = []

    def push(self,item: T) ->None:
        #Add an item to the top of the stack
        self.stack.append(item)

    def pop(self) -> T:
        #Remove an item from the top of the stack
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        #Return the top item from the stack without removing it
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("peek from an empty stack")
    
    def is_empty(self) -> bool:
        #Check if the stack is empty
        return len(self.stack) == 0
    
    def size(self) -> int:
        #Return the number of items in the stack
        return len(self.stack)

if __name__ == "__main__":
    #Create a stack for integers
    stack = Stack[int]()
    #Push items onto the stack
    stack.push(1)
    stack.push(2)
    print("Integers Stack Top:",stack.peek())

    #Create a stack for strings
    stack_str = Stack[str]()
    #Push items onto the stack
    stack_str.push("Apple")
    stack_str.push("Banana")
    print("Strings Stack Top:",stack_str.peek())
