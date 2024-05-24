# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def dfs(cloned_node, target_node):
            # Declare 'ans' as nonlocal to modify the 'ans' defined in 'getTargetCopy'.
            nonlocal result

            if cloned_node:
                # Check if the current node is the target node
                if cloned_node.val == target_node.val:
                    result = cloned_node
                    return
                
                # Recurse on the left and right subtrees
                dfs(cloned_node.left, target_node)
                dfs(cloned_node.right, target_node)

        result = None  # Initialize the result variable
        dfs(cloned, target)  # Start DFS on the cloned tree
        return result  # Return the found node



# class Solution:
#     def inorder(self, root, data, result):
#         if root:
#             print(root.val, data)
#             self.inorder(root.left, data, result)
#             if data == root.val:
#                 # print(root.val)
#                 result.append(root)
#                 return 
#             self.inorder(root.right, data, result)
        

#     def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
#         data = target.val
#         result = []
       
#         self.inorder(cloned, data, result)
#         return result[0]  