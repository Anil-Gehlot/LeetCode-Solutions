# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def inOrder(self, root, queue):
        if root:
            self.inOrder(root.left, queue)
            queue.append(root.val)
            self.inOrder(root.right, queue)

    def __init__(self, root: Optional[TreeNode]):
        self.queue = deque()
        self.inOrder(root, self.queue)

    def next(self) -> int:
        return self.queue.popleft()
        

    def hasNext(self) -> bool:
        return len(self.queue) != 0 
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()