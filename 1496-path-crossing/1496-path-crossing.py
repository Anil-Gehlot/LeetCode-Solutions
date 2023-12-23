class Solution:
    def isPathCrossing(self, path: str) -> bool:

        # Initialize starting coordinates
        x_coordinate = 0 
        y_coordinate = 0

        # Use a set to store visited coordinates
        direction_set = {(0, 0)}

        # Iterate through each direction in the path
        for direction in path:

            # Update coordinates based on the direction
            if direction == "E":
                x_coordinate += 1
            elif direction == "W":
                x_coordinate -= 1
            elif direction == "N":
                y_coordinate += 1
            elif direction == "S":
                y_coordinate -= 1
            
            # Create a tuple representing the current move
            move = (x_coordinate, y_coordinate)

            # Check if the current move has been visited before
            if move not in direction_set:
                
                # If not, add it to the set of visited coordinates
                direction_set.add(move)
            else:
                
                # If the move has been visited before, the path crosses itself
                return True

        # If the entire path is traversed without crossing, return False
        return False
