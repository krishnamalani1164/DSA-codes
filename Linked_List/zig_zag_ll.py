class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def reverse(head):
    prev = None
    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev

def zigzag_reorder(head):
    if not head or not head.next:
        return head

    mid = find_middle(head)
    second = reverse(mid.next)
    mid.next = None  # break the list

    first = head
    while second:
        temp1 = first.next
        temp2 = second.next

        first.next = second
        second.next = temp1

        first = temp1
        second = temp2

# List: 1 → 2 → 3 → 4 → 5
# Output: 1 → 5 → 2 → 4 → 3

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
a.next = b; b.next = c; c.next = d; d.next = e

zigzag_reorder(a)

def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

print_list(a)