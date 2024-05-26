# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self, root, result):
        
        # Perform in-order traversal and append values to the result list
        if root:
            self.inOrder(root.left, result)
            result.append(root.val)
            self.inOrder(root.right, result)

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        values = []
        # Populate the values list with in-order traversal
        self.inOrder(root, values)

        # Initialize the minimum difference as infinity
        min_val = math.inf

        # Compute the minimum difference between consecutive values
        for k in range(1, len(values)):
            diff = values[k] - values[k - 1]
            if diff < min_val:
                min_val = diff

        # Return the minimum difference found
        return min_val
