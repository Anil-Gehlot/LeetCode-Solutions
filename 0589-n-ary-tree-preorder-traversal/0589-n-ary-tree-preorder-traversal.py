"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def recursive_preorder(self, root, result):
        
        # append the root value in the result
        if root :
            result.append(root.val)

            # if there exist children of root visit them
            if root.children:

                for child in root.children:
                    # recursively calling function for each child
                    self.recursive_preorder(child, result)

    def preorder(self, root: 'Node') -> List[int]:
        result = []

        self.recursive_preorder(root, result)
        return result
