# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recursiveInorder(self, root, result):
        
        # If the current node is not None, proceed with the inorder traversal
        if root:
            
            # Traverse the left subtree first
            self.recursiveInorder(root.left, result)
            
            # Visit the root node
            result.append(root.val)
            
            # Traverse the right subtree
            self.recursiveInorder(root.right, result)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        
        # Call the recursive helper function to perform the traversal
        self.recursiveInorder(root, result)
        return result