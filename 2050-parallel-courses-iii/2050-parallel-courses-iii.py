import collections
from typing import List

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # Create an empty graph with n vertices.
        graph = [[] for _ in range(n)]

        # Initialize an array to store the in-degrees of each vertex.
        inDegree = [0] * n

        # Initialize a distance array with the times for each task.
        dist = time.copy()

        # Build the directed graph based on the provided relations.
        for a, b in relations:
            u = a - 1  # Adjust the vertex index to 0-based indexing.
            v = b - 1  # Adjust the vertex index to 0-based indexing.
            graph[u].append(v)  # Add a directed edge from u to v.
            inDegree[v] += 1  # Increment the in-degree of vertex v.

        # Topological Sorting using a queue.
        q = collections.deque([i for i, d in enumerate(inDegree) if d == 0])

        # Perform a topological sort to find the minimum time required.
        while q:
            u = q.popleft()  # Dequeue a vertex with in-degree 0.
            for v in graph[u]:
                # Update the maximum time for each adjacent vertex.
                dist[v] = max(dist[v], dist[u] + time[v])
                inDegree[v] -= 1  # Decrement the in-degree of vertex v.
                if inDegree[v] == 0:
                    q.append(v)  # If in-degree becomes 0, enqueue the vertex.

        # Return the maximum time as the result.
        return max(dist)
