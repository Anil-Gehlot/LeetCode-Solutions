
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # Check if source and target are the same
        if source == target:
            return 0

        # Create a dictionary to map each stop to the list of bus routes passing through that stop
        stop_to_routes = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].append(i)

        # Initialize sets to keep track of visited stops and routes
        visited_stops = set()
        visited_routes = set()

        # Initialize the queue with the source stop
        queue = [source]
        num_buses = 0  # Initialize the number of buses taken

        while queue:
            new_queue = []  # Initialize a new queue for the next level of stops

            # Iterate through stops in the current level
            for current_stop in queue:
                # Iterate through bus routes passing through the current stop
                for route_index in stop_to_routes[current_stop]:
                    # If the bus route has not been visited
                    if route_index not in visited_routes:
                        visited_routes.add(route_index)  # Mark the bus route as visited

                        # Iterate through stops along the bus route
                        for next_stop in routes[route_index]:
                            # If the target stop is reached
                            if next_stop == target:
                                return num_buses + 1  # Return the number of buses taken

                            # If the stop has not been visited
                            if next_stop not in visited_stops:
                                visited_stops.add(next_stop)  # Mark the stop as visited
                                new_queue.append(next_stop)  # Add the stop to the new queue

            queue = new_queue  # Update the queue for the next iteration
            num_buses += 1  # Increment the number of buses taken

        return -1  # Return -1 if the target stop is not reachable
