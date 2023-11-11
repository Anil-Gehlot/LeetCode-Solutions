class Graph:
    def __init__(self, n, edges):
        self.graph = {i: [] for i in range(n)}
        self.addEdges(edges)

    def addEdges(self, edges):
        for edge in edges:
            from_node, to_node, cost = edge
            self.graph[from_node].append((to_node, cost))

    def shortestPath(self, node1, node2):
        pq = [(0, node1)]
        visited = set()

        while pq:
            current_cost, current_node = heapq.heappop(pq)

            if current_node in visited:
                continue

            visited.add(current_node)

            if current_node == node2:
                return current_cost

            for neighbor, cost in self.graph[current_node]:
                heapq.heappush(pq, (current_cost + cost, neighbor))

        return -1

    def addEdge(self, edge):
        from_node, to_node, cost = edge
        self.graph[from_node].append((to_node, cost))

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)