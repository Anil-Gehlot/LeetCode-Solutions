# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # Define a function 'dfs' for depth-first search and mode counting
        def dfs(node, counter):
            # Base case: If the node is None, return and do nothing
            if not node:
                return
            
            # Increment the counter for the current node's value
            counter[node.val] += 1
            
            # Recursively traverse the left and right subtrees
            dfs(node.left, counter)
            dfs(node.right, counter)
        
        # Create a dictionary 'counter' to store the frequency of each node's value
        counter = defaultdict(int)
        
        # Start the depth-first search from the 'root' node
        dfs(root, counter)
        
        # Find the maximum frequency of any node's value
        max_freq = max(counter.values())
        
        # Initialize an empty list to store the mode(s)
        ans = []
        
        # Iterate through the keys in the 'counter' dictionary
        for key in counter:
            # If the frequency of the current key matches the maximum frequency,
            # add it to the 'ans' list as a mode
            if counter[key] == max_freq:
                ans.append(key)
        
        # Return the list of mode(s)
        return ans
