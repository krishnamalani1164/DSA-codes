class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Helper function to merge two sorted linked lists
def merge(l1, l2):
    dummy = Node(-1)
    tail = dummy
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next

# Function to find the middle of the list
def get_middle(head):
    slow = fast = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    if prev:
        prev.next = None  # Split the list
    return slow

# Merge sort function
def merge_sort(head):
    if not head or not head.next:
        return head
    mid = get_middle(head)
    left = merge_sort(head)
    right = merge_sort(mid)
    return merge(left, right)


def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Creating unsorted linked list
a = Node(4)
b = Node(2)
c = Node(1)
d = Node(3)

a.next = b
b.next = c
c.next = d

# Sort the list
sorted_head = merge_sort(a)
print_list(sorted_head)  # Output: 1 -> 2 -> 3 -> 4 -> None