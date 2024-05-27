"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        # If the root is None, return an empty list
        if root is None:
            return []

        result = [[root.val]]  # Initialize the result with the root node's value

        queue = deque()  # Initialize an empty deque for BFS
        queue.append(root)  # Start with the root node
        
        while queue:
            
            temp_result = []  # List to store the values of nodes at the current level
            temp_child = []  # List to store the child nodes for the next level

            # Process all nodes at the current level
            for node in queue:
                for child in node.children:  # Iterate over all children of the current node
                    temp_child.append(child)  # Add the child to the temp_child list
                    temp_result.append(child.val)  # Add the child's value to temp_result
            
            queue = temp_child  # Move to the next level by updating the queue to temp_child

            if temp_result:  # If there are nodes at the current level, add their values to the result
                result.append(temp_result)
                
        return result  # Return the final level order traversal result
