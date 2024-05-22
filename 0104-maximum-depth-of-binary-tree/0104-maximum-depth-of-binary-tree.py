# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # Base case: if the tree is empty, the depth is 0
        if root is None:
            return 0

        # Recursively find the depth of the left subtree
        left = self.maxDepth(root.left)

        # Recursively find the depth of the right subtree
        right = self.maxDepth(root.right)

        # The depth of the current node is the maximum depth of the left or right subtrees, plus 1 for the current node
        return max(left, right) + 1   