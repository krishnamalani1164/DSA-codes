class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

# Example usage:
if __name__ == "__main__":
    ll = LinkedList()
    ll.push_front(30)
    ll.push_front(20)
    ll.push_front(10)

    print("Original list:")
    ll.print_list()

    ll.reverse()

    print("Reversed list:")
    ll.print_list()