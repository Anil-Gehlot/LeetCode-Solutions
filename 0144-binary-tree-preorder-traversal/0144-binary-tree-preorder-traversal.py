# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def recursivePreorder(self, root, result):
        
        # If the current node is not None, proceed with the preorder traversal
        if root:
            
            # Visit the root node first
            result.append(root.val)
            
            # Traverse the left subtree
            self.recursivePreorder(root.left, result)
            
            # Traverse the right subtree
            self.recursivePreorder(root.right, result)
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        
        # Call the recursive helper function to perform the traversal
        self.recursivePreorder(root, result)
        return result