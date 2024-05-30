# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preOrder(self, root, low, high, range_sum):
        if root:
            if low <= root.val <= high:
                range_sum[0] += root.val
            
            self.preOrder(root.left, low, high, range_sum)
            self.preOrder(root.right, low, high, range_sum)

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        range_sum = [0]

        self.preOrder(root, low, high, range_sum)

        return range_sum[0]