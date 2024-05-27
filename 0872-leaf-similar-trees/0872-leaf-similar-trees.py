# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # perform pre-order traversal
    def preOrder(self, root, result):
        if root:
            if root.left is None and root.right is None:  
                result.append(root.val) 
            self.preOrder(root.left, result)  
            self.preOrder(root.right, result)  

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        root1_result = []  # Initialize list to store leaf values of root1
        root2_result = []  # Initialize list to store leaf values of root2

        # Perform pre-order traversal to extract leaf values of root1
        self.preOrder(root1, root1_result)

        # Perform pre-order traversal to extract leaf values of root2
        self.preOrder(root2, root2_result)

        # Compare leaf value sequences of both trees
        return root1_result == root2_result
