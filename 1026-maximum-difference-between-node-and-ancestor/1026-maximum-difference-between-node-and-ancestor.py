# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.maxAncestorDiffHelper(root, root.val, root.val)

    def maxAncestorDiffHelper(self, root: TreeNode, mini: int, maxi: int) -> int:
        if root is None:
            return 0
        mini = min(mini, root.val)
        maxi = max(maxi, root.val)
        l = self.maxAncestorDiffHelper(root.left, mini, maxi)
        r = self.maxAncestorDiffHelper(root.right, mini, maxi)
        return max(maxi - mini, max(l, r))
