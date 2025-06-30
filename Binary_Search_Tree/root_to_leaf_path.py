class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def print_root_to_leaf_paths(root, path=[]):
    if not root:
        return
    
    # Append current node to path
    path.append(root.val)
    
    # If it's a leaf node, print the path
    if not root.left and not root.right:
        print(" -> ".join(map(str, path)))
    
    # Recursively traverse left and right subtrees
    print_root_to_leaf_paths(root.left, path[:])
    print_root_to_leaf_paths(root.right, path[:])

# Example Usage:
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(20)

print_root_to_leaf_paths(root)