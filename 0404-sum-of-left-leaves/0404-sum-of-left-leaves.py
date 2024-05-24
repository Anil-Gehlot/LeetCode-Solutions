# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursiveSum(self, root, is_left):
        if root is None:
            return 0
        
        # Check if it is a left leaf
        if root.left is None and root.right is None and is_left:
            return root.val
        
        # Recursively sum left leaves for both subtrees
        left = self.recursiveSum(root.left, True)
        right = self.recursiveSum(root.right, False)
        
        return left + right

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.recursiveSum(root, False)  # False because root itself is not a left child
