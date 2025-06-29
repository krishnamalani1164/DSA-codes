class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Push to front
    def push_front(self, val):
        new_node = Node(val)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    # Pop from front
    def pop_front(self):
        if not self.head:
            print("List is empty.")
            return None
        val = self.head.val
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        return val

    def display(self):
        curr = self.head
        while curr:
            print(curr.val, end=" <-> ")
            curr = curr.next
        print("None")

dll = DoublyLinkedList()

dll.push_front(10)
dll.push_front(20)
dll.push_front(30)
dll.display()     # Output: 30 <-> 20 <-> 10 <-> None

print(dll.pop_front())  # Output: 30
dll.display()           # Output: 20 <-> 10 <-> None