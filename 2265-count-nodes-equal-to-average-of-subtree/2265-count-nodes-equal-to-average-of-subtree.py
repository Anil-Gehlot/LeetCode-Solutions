# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
class Solution:
  def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
    ans = 0  # Initialize a variable to count valid subtrees

    def dfs(root: Optional[TreeNode]) -> Tuple[int, int]:
      nonlocal ans  # Use 'nonlocal' to modify 'ans' from the outer scope
      if not root:
        return (0, 0)  # If the current node is None, return 0 for sum and count
      leftSum, leftCount = dfs(root.left)  # Recursively calculate sum and count of the left subtree
      rightSum, rightCount = dfs(root.right)  # Recursively calculate sum and count of the right subtree
      summ = root.val + leftSum + rightSum  # Calculate the sum of the current subtree
      count = 1 + leftCount + rightCount  # Calculate the total count of nodes in the subtree
      if summ // count == root.val:  # Check if the subtree's average is equal to the root's value
        ans += 1  # If it is, increment the count of valid subtrees
      return (summ, count)  # Return the sum and count of the current subtree

    dfs(root)  # Start the depth-first search from the root node
    return ans  # Return the total count of valid subtrees
