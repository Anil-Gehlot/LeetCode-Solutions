# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # function to perform preorder traversal
    def preOrder(self, root, result):

        # If the current node is None, append a placeholder to the result list
        if root is None:
            result.append(" ")

        # If the current node exists, append its value to the result list
        if root:
            result.append(root.val)

            # Recursively call preOrder for the left and right subtree
            self.preOrder(root.left, result)
            self.preOrder(root.right, result)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Initialize empty lists to store the traversal results for both trees
        p_tree = []
        q_tree = []

        # Perform preorder traversal for tree p and append the results to p_tree list
        self.preOrder(p, p_tree)
        # Perform preorder traversal for tree q and append the results to q_tree list
        self.preOrder(q, q_tree)

        # Check if the traversal lists are equal and return the result
        return p_tree == q_tree
