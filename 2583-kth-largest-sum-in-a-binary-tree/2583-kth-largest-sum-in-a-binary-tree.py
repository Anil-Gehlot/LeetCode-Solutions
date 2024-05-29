# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderTraverse(self, root: Optional[TreeNode], levels_sum: List[int]):
        # If the root is None, there is nothing to traverse
        if root is None:
            return
        
        # Initialize a queue for BFS
        queue = deque()
        queue.append(root)

        # Perform BFS
        while queue:
            temp_sum = 0
            temp_queue = deque()

            # Process all nodes at the current level
            for node in queue:
                temp_sum += node.val
                # Add child nodes of the current level to the temp queue
                if node.left:
                    temp_queue.append(node.left)
                if node.right:
                    temp_queue.append(node.right)

            # Move to the next level
            queue = temp_queue
            # Store the sum of the current level
            levels_sum.append(temp_sum)

    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        levels_sum = []

        # Perform level order traversal and collect level sums
        self.levelOrderTraverse(root, levels_sum)
        
        # Sort the level sums in descending order
        levels_sum.sort(reverse=True)
        
        # Check if there are fewer levels than k
        if k > len(levels_sum):
            return -1
        
        # Return the k-th largest level sum
        return levels_sum[k - 1]