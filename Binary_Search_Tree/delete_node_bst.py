class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTModifier:
    def delete_node(self, root, key):
        """Deletes a node using inorder successor logic"""
        if not root:
            return None
        
        # Locate the node to delete
        if key < root.val:
            root.left = self.delete_node(root.left, key)
        elif key > root.val:
            root.right = self.delete_node(root.right, key)
        else:
            # Case 1: No child (leaf node)
            if not root.left and not root.right:
                return None
            # Case 2: One child
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # Case 3: Two children -> Find inorder successor
            successor = self.find_min(root.right)
            root.val = successor.val  # Replace with successor
            root.right = self.delete_node(root.right, successor.val)  # Delete successor
        
        return root

    def find_min(self, node):
        """Finds the inorder successor (smallest node in right subtree)"""
        while node.left:
            node = node.left
        return node