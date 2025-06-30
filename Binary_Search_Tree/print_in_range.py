class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def print_in_range(root, start, end):
    if not root:
        return
    
    if root.val > start:
        print_in_range(root.left, start, end)

    if start <= root.val <= end:
        print(root.val, end=" ")

    if root.val < end:
        print_in_range(root.right, start, end)

# Example Usage:
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(20)

print_in_range(root, 5, 15)  # Output: 5 7 10 12 15