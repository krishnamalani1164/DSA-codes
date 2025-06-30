class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def build_bst(arr):
    root = None
    for value in arr:
        root = insert(root, value)
    return root

# Example usage
arr = [10, 5, 15, 3, 7, 13, 18]
bst_root = build_bst(arr)