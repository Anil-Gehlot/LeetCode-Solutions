class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        # Initialize an array to store in-degrees of nodes and set the root to -1
        inDegree = [0] * n
        root = -1

        # Calculate in-degree for each child and check for multiple edges to a node
        for child in leftChild:
            if child != -1:
                inDegree[child] += 1
                if inDegree[child] == 2:
                    return False

        for child in rightChild:
            if child != -1:
                inDegree[child] += 1
                if inDegree[child] == 2:
                    return False

        # Find the root (node with in-degree == 0) and check for multiple roots
        for i in range(n):
            if inDegree[i] == 0:
                if root == -1:
                    root = i
                else:
                    return False  # Multiple roots

        # If no root found, return false
        if root == -1:
            return False

        # Check if the count of nodes reachable from the root is equal to n
        return self.countNodes(root, leftChild, rightChild) == n

    def countNodes(self, root, leftChild, rightChild):
        # Recursively count nodes starting from the root
        if root == -1:
            return 0
        return 1 + self.countNodes(leftChild[root], leftChild, rightChild) + self.countNodes(rightChild[root], leftChild, rightChild)
