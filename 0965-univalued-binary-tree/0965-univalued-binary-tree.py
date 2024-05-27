# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    # pre-order traversal
    def preOrder(self, root, result):
        if root:
            result.add(root.val)
            self.preOrder(root.left, result)
            self.preOrder(root.right, result)

    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        result = set()  # Initialize an empty set to store unique values

        self.preOrder(root, result)  # Perform a pre-order traversal of the tree

        # Check if there is exactly one unique value in the set
        return len(result) == 1