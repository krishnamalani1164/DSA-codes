class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_back(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def remove_nth_from_end(self, n):
        dummy = Node(0)
        dummy.next = self.head
        first = second = dummy

        for _ in range(n + 1):
            if not first:
                print("List is shorter than n")
                return
            first = first.next

        while first:
            first = first.next
            second = second.next

        to_delete = second.next
        second.next = second.next.next

        if to_delete == self.head:
            self.head = self.head.next
        if to_delete == self.tail:
            self.tail = second if second.next is None else self.tail

        to_delete = None

# Example usage:
if __name__ == "__main__":
    ll = LinkedList()
    for val in [10, 20, 30, 40, 50]:
        ll.push_back(val)

    print("Original list:")
    ll.print_list()

    n = 2
    print(f"Removing the {n}th node from the end...")
    ll.remove_nth_from_end(n)

    print("Updated list:")
    ll.print_list()