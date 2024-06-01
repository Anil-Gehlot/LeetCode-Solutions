# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        # If it is a leaf node, return its value (0 or 1)
        if root.left is None and root.right is None:
            return bool(root.val)

        # Recursively evaluate the left and right children
        left_value = self.evaluateTree(root.left)
        right_value = self.evaluateTree(root.right)

        # Apply the boolean operation based on the current node's value
        if root.val == 2:  # OR operation
            return left_value or right_value
        elif root.val == 3:  # AND operation
            return left_value and right_value