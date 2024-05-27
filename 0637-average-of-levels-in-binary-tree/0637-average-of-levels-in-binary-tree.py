# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        # If the root is None, return an empty list as there are no nodes to traverse
        if root is None:
            return []
        
        result = []  # This will store the final average value of the same level nodes 
        
        queue = deque()  # Initialize a deque to use as a queue for BFS
        queue.append(root)  # Start with the root node
        
        while queue:
            temp_res = []  # List to store the values of nodes at the current level
            temp_child = []  # List to store the child nodes for the next level
            
            # Iterate through nodes at the current level
            for node in queue:
                temp_res.append(node.val)  # Add the value of the current node to temp_res
                if node.left:  # If the current node has a left child, add it to temp_child
                    temp_child.append(node.left)
                if node.right:  # If the current node has a right child, add it to temp_child
                    temp_child.append(node.right)
            
            result.append(sum(temp_res) / len(temp_res) )  # Add the average value of the current level nodes on to the result list
            queue = temp_child  # Move to the next level by setting queue to temp_child
        
        return result