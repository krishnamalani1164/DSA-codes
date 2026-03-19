class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def removeCycle(head):
    slow = fast = head

    # Step 1: Detect the cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return  # No cycle

    # Step 2: Find start of the cycle
    slow = head
    prev = None  # To track the node before fast
    while slow != fast:
        prev = fast
        slow = slow.next
        fast = fast.next

    # Step 3: Remove the cycle
    prev.next = None

# Example usage:
# Create nodes
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

# Connect nodes to form a cycle
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # cycle here

removeCycle(node1)

# Traverse to confirm cycle is removed
def printList(head):
    visited = set()
    while head:
        if head in visited:
            print("Cycle detected again.")
            break
        print(head.val, end=" -> ")
        visited.add(head)
        head = head.next
    else:
        print("None")

printList(node1)  # Output: 3 → 2 → 0 → -4 → None