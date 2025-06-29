class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next          # move 1 step
        fast = fast.next.next     # move 2 steps
        if slow == fast:
            return True           # cycle detected
    return False                  # no cycle

# Step 1: Create nodes
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

# Step 2: Link nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # cycle here

# Step 3: Check for cycle
print(hasCycle(node1))  # Output: True