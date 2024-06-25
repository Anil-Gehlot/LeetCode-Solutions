# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root, result):
        if root:
            self.inorderTraversal(root.left, result)
            result.append(root.val)
            self.inorderTraversal(root.right, result)

    def inorderTraversal1(self, root, result):
        
        if root:
            self.inorderTraversal1(root.left, result)
    
            sum = 0
            for i in range(len(result)-1, -1, -1):

                # print(result[i], root.val)
                if result[i] > root.val:
                    sum += result[i]
                elif result[i] == root.val:
                    sum += result[i]
                    break
            
            root.val = sum
            
            self.inorderTraversal1(root.right, result)

    def bstToGst(self, root: TreeNode) -> TreeNode:
        result = []
        self.inorderTraversal(root, result)
        
        self.inorderTraversal1(root, result)
        return root

        
        