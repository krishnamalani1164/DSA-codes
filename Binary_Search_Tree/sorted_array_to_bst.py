class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sorted_array_to_bst(arr):
    if not arr:
        return None
    
    mid = len(arr) // 2
    root = TreeNode(arr[mid])
    
    root.left = sorted_array_to_bst(arr[:mid])
    root.right = sorted_array_to_bst(arr[mid+1:])
    
    return root

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7]
root = sorted_array_to_bst(arr)