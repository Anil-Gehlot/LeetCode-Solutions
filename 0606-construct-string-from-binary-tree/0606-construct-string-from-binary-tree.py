# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        # Base case: if the root is None, return an empty string
        if not root:
            return ""

        # Convert the root value to a string
        result = str(root.val)

        # Recursively get the string representation of the left and right subtrees
        l = self.tree2str(root.left)
        r = self.tree2str(root.right)

        # If the root has no children, return its value as a string
        if not root.left and not root.right:
            return result

        # If the root has no right child, include only the left subtree in the result
        if not root.right:
            return result + "(" + l + ")"

        # If the root has no left child, include empty parentheses for the left subtree
        if not root.left:
            return result + "()" + "(" + r + ")"

        # If the root has both left and right children, include both subtrees in the result
        return result + "(" + l + ")" + "(" + r + ")"