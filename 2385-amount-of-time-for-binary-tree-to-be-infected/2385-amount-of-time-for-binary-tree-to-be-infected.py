# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        ans = -1
        graph = self._getGraph(root)
        q = collections.deque([start])
        seen = {start}

        while q:
            ans += 1
            for _ in range(len(q)):
                u = q.popleft()
                for v in graph[u]:
                    if v not in seen:
                        q.append(v)
                        seen.add(v)

        return ans

    def _getGraph(self, root: Optional[TreeNode]) -> Dict[int, List[int]]:
        graph = collections.defaultdict(list)
        q = collections.deque([(root, -1)])  # (node, parent)

        while q:
            node, parent = q.popleft()
            if parent != -1:
                graph[parent].append(node.val)
                graph[node.val].append(parent)
            if node.left:
                q.append((node.left, node.val))
            if node.right:
                q.append((node.right, node.val))

        return graph