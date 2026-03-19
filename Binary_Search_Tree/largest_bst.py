class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTInfo:
    def __init__(self, is_bst, size, min_val, max_val):
        self.is_bst = is_bst
        self.size = size
        self.min_val = min_val
        self.max_val = max_val

def largest_bst_size(root):
    def helper(node):
        if not node:
            return BSTInfo(True, 0, float('inf'), float('-inf'))
        
        left_info = helper(node.left)
        right_info = helper(node.right)

        # Check if current subtree is a BST
        if left_info.is_bst and right_info.is_bst and left_info.max_val < node.val < right_info.min_val:
            return BSTInfo(True, left_info.size + right_info.size + 1, 
                           min(node.val, left_info.min_val), 
                           max(node.val, right_info.max_val))
        
        return BSTInfo(False, max(left_info.size, right_info.size), 0, 0)
    
    return helper(root).size

# Example usage:
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(1)
root.left.right = TreeNode(8)
root.right.right = TreeNode(7)  # This node violates BST property

print("Size of the Largest BST:", largest_bst_size(root))