# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inorderTraversal(self, root, result, flag):
        if root:
            self.inorderTraversal(root.left, result, flag)

            if flag == 1:
                sum = 0
                for i in range(len(result)-1, -1, -1):

                    if result[i] > root.val:
                        sum += result[i]
                    elif result[i] == root.val:
                        sum += result[i]
                        break

                root.val = sum
            else:
                result.append(root.val)
                
            self.inorderTraversal(root.right, result, flag)

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        result = []
        self.inorderTraversal(root, result, 0)
        
        self.inorderTraversal(root, result, 1)
        return root