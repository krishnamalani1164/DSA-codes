class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    result = []
    
    def traverse(node):
        if node:
            traverse(node.left)
            result.append(node.val)
            traverse(node.right)
    
    traverse(root)
    return result

def sortedArrayToBST(arr, left, right):
    if left > right:
        return None

    mid = (left + right) // 2
    node = TreeNode(arr[mid])

    node.left = sortedArrayToBST(arr, left, mid - 1)
    node.right = sortedArrayToBST(arr, mid + 1, right)

    return node

def mergeBSTs(root1, root2):
    arr1 = inorderTraversal(root1)
    arr2 = inorderTraversal(root2)
    merged = sorted(arr1 + arr2)  # Directly merge and sort both arrays
    return sortedArrayToBST(merged, 0, len(merged) - 1)

# Example usage:
root1 = TreeNode(2, TreeNode(1), TreeNode(4))
root2 = TreeNode(3, TreeNode(0), TreeNode(5))

merged_root = mergeBSTs(root1, root2)