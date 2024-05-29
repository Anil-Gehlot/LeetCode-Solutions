# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrderTraverse(self, root: Optional[TreeNode], levels_sum: List[int]):
        # Initialize a queue with the root node for BFS.
        queue = deque([root])

        # Perform BFS until the queue is empty.
        while queue:
            # Initialize the sum for the current level.
            temp_sum = 0
            # Initialize a temporary queue for the next level.
            temp_queue = deque()

            # Process all nodes at the current level.
            for node in queue:
                # Add the value of the current node to the level sum.
                temp_sum += node.val
                # Add the left child to the temporary queue if it exists.
                if node.left:
                    temp_queue.append(node.left)
                # Add the right child to the temporary queue if it exists.
                if node.right:
                    temp_queue.append(node.right)
            
            # Append the sum of the current level to levels_sum.
            levels_sum.append(temp_sum)
            # Move to the next level.
            queue = temp_queue

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        # List to store sums of each level.
        levels_sum = []

        # Calculate level sums using levelOrderTraverse.
        self.levelOrderTraverse(root, levels_sum)
        
        
        # Find the index of the maximum level sum and return the 1-based level.
        return levels_sum.index(max(levels_sum)) + 1