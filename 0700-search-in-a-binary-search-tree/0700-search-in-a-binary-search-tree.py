# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        # Base case
        if root is None or root.val == val:
            return root
        
        # If val is greater than root's value, search in the right subtree
        if val > root.val:
            return self.searchBST(root.right, val)
        
        # If val is less than root's value, search in the left subtree
        elif val < root.val:
            return self.searchBST(root.left, val) 