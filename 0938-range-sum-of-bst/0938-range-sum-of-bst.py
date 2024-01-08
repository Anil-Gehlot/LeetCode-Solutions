# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        # Helper function for depth-first search (dfs)
        def dfs(node):
            # Base case: if the node is None, return 0
            if not node:
                return 0
            
            # Initialize current_val to 0
            current_val = 0
            
            # Check if the node's value is within the specified range [low, high]
            if low <= node.val <= high:
                current_val = node.val
            
            # Recursively traverse the left subtree only if the node's value is greater than low
            left_val = dfs(node.left) if node.val > low else 0
            
            # Recursively traverse the right subtree only if the node's value is less than high
            right_val = dfs(node.right) if node.val < high else 0
            
            # Return the sum of current value, left subtree sum, and right subtree sum
            return current_val + left_val + right_val
        
        # Call the dfs function with the root of the binary search tree
        return dfs(root)