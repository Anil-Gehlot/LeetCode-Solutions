# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    # function to perform inorder traversal and count nodes
    def inorder(self, root, result):
        # If the current node is not None, traverse its children
        if root:
            # Traverse the left subtree
            self.inorder(root.left, result)
            # Increment the node count
            result[0] = result[0] + 1
            # Traverse the right subtree
            self.inorder(root.right, result)
    
    # function to count the total number of nodes in the tree
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # Initialize result as a list with one element, set to 0
        # This allows us to pass the count by reference
        result = [0]
        
        # Perform inorder traversal starting from the root
        self.inorder(root, result)
        
        # Return the final count of nodes
        return result[0]