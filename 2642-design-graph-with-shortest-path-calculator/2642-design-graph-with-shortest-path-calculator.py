class Graph:
    def __init__(self, n, edges):
        # Initialize the graph with n nodes and an empty adjacency list for each node
        self.graph = {i: [] for i in range(n)}
        
        # Add the edges to the graph during initialization
        self.addEdges(edges)

    def addEdges(self, edges):
        # Add edges to the graph
        for edge in edges:
            from_node, to_node, cost = edge
            self.graph[from_node].append((to_node, cost))

    def shortestPath(self, node1, node2):
        # Priority queue to store (cost, node) pairs for Dijkstra's algorithm
        pq = [(0, node1)]
        
        # Set to keep track of visited nodes
        visited = set()

        while pq:
            # Get the node with the minimum cost from the priority queue
            current_cost, current_node = heapq.heappop(pq)

            # Skip if the node has already been visited
            if current_node in visited:
                continue

            # Mark the current node as visited
            visited.add(current_node)

            # If the current node is the destination, return the cost
            if current_node == node2:
                return current_cost

            # Explore neighbors of the current node
            for neighbor, cost in self.graph[current_node]:
                # Add the neighbor to the priority queue with updated cost
                heapq.heappush(pq, (current_cost + cost, neighbor))

        # If no path is found, return -1
        return -1

    def addEdge(self, edge):
        # Add a new edge to the graph
        from_node, to_node, cost = edge
        self.graph[from_node].append((to_node, cost))

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)