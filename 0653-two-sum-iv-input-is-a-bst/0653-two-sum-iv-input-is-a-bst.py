# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # inorder traversal method
    def inorderTraverse(self, root, result):
        if root:
            self.inorderTraverse(root.left, result)
            result.append(root.val)
            self.inorderTraverse(root.right, result)
        
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        result = []

        # Perform in-order traversal to get the sorted list of node values
        self.inorderTraverse(root, result)

        # Initialize two pointers
        start, end = 0, len(result) - 1

        # Use two-pointer technique to find if there exist two numbers that sum to k
        while start < end:
            current_sum = result[start] + result[end]
            if current_sum == k:
                return True
            elif current_sum < k:
                start += 1
            else:
                end -= 1

        # If no such pair is found, return False
        return False

        