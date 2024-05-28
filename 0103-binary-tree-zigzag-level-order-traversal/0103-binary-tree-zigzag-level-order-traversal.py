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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # If the root is None, the tree is empty, so return an empty list
        if root is None:
            return []

        result = []  # This will store the final zigzag level order traversal
        queue = deque()  # Initialize the queue with deque to facilitate level order traversal
        queue.append(root)  # Start with the root node in the queue

        while queue:
            temp_res = []  # This will store the values of nodes at the current level
            temp_child = []  # This will store the children of the nodes at the current level
            
            # Process each node in the current level
            for node in queue:
                temp_res.append(node.val)  # Append the current node's value to the level result
                
                # Append children to temp_child list
                if node.left:
                    temp_child.append(node.left)
                if node.right:
                    temp_child.append(node.right)

            result.append(temp_res)  # Add the level result to the final result
            queue = temp_child  # Move to the next level by replacing the queue with temp_child

        # Reverse the values of nodes at every other level to achieve the zigzag pattern
        for i in range(len(result)):
            if i % 2 != 0:
                result[i] = result[i][::-1]

        return result  # Return the final zigzag level order traversal