class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Step 1: Perform an inorder traversal to store the BST elements in a sorted list
def inorder_traversal(root, nodes):
    if root is None:
        return
    inorder_traversal(root.left, nodes)
    nodes.append(root.val)
    inorder_traversal(root.right, nodes)

# Step 2: Convert sorted list to balanced BST
def sorted_array_to_bst(arr):
    if not arr:
        return None

    mid = len(arr) // 2
    root = TreeNode(arr[mid])

    root.left = sorted_array_to_bst(arr[:mid])
    root.right = sorted_array_to_bst(arr[mid+1:])

    return root

# Function to balance an unbalanced BST
def balance_bst(root):
    nodes = []
    inorder_traversal(root, nodes)  # Get sorted values
    return sorted_array_to_bst(nodes)  # Build a balanced BST

# Example usage:
# Creating an unbalanced BST
root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right = TreeNode(15)
root.right.right = TreeNode(20)

# Balancing the BST
balanced_root = balance_bst(root)

# Function to print inorder traversal of the balanced BST
def print_inorder(root):
    if root is None:
        return
    print_inorder(root.left)
    print(root.val, end=" ")
    print_inorder(root.right)

print("Inorder Traversal of Balanced BST:")
print_inorder(balanced_root)