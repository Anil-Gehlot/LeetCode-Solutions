# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recursivePostorder(self, root, result):
        
        # If the current node is not None, proceed with the postorder traversal
        if root:
            
            # Traverse the left subtree first
            self.recursivePostorder(root.left, result)
            # Traverse the right subtree
            self.recursivePostorder(root.right, result)
            # Visit the root node last
            result.append(root.val)
    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        # Call the recursive helper function to perform the traversal
        self.recursivePostorder(root, result)
        return result