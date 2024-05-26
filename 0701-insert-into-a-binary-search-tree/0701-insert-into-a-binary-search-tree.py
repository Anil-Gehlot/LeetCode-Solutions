# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        # If the root is None, create a new node with the given value and return it
        if root is None:
            return TreeNode(val)
        
        # If the value to insert is less than the root value
        if val < root.val:
            
            # If there is a left child, continue recursion to the left subtree
            if root.left is not None:
                self.insertIntoBST(root.left, val)
                
            # If there is no left child, insert the new node here
            else:
                root.left = TreeNode(val)
        
        # If the value to insert is greater than the root value
        if val > root.val:
            
            # If there is a right child, continue recursion to the right subtree
            if root.right is not None:
                self.insertIntoBST(root.right, val)
                
            # If there is no right child, insert the new node here
            else:
                root.right = TreeNode(val)
        
        # Return the root after insertion
        return root