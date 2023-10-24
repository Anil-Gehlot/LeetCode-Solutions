# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []  # If the tree is empty, return an empty list.

        ans = []  # Initialize an empty list to store the maximum values at each level.
        q = collections.deque([root])  # Initialize a queue with the root node.

        while q:
            maxi = -math.inf  # Initialize the maximum value to negative infinity.
            for _ in range(len(q)):
                root = q.popleft()  # Remove the front node from the queue.
                maxi = max(maxi, root.val)  # Update the maximum value at this level.
                if root.left:
                    q.append(root.left)  # Add the left child to the queue if it exists.
                if root.right:
                    q.append(root.right)  # Add the right child to the queue if it exists.
            ans.append(maxi)  # Add the maximum value at this level to the answer list.

        return ans  # Return the list of maximum values at each level of the tree.

        