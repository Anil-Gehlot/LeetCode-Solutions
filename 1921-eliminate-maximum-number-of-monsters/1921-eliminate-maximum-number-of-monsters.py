class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # Create an empty list to store the time it takes for each monster to reach the city
        time = []
        
        # Calculate the time it takes for each monster to reach the city and add it to the 'time' list
        for distance, speeds in zip(dist, speed):
            # Use math.ceil to round up to the nearest minute
            time.append(math.ceil(distance/speeds))
        
        # Sort the 'time' list in ascending order
        time.sort()
        
        # Initialize a variable to keep track of the number of monsters you can eliminate
        kill_monster = 0
        
        # Iterate through the 'time' list and check if you can eliminate monsters before they reach the city
        for distance in range(len(time)):
            # If the time it takes for a monster to reach the city is less than or equal to the index,
            # it means you can eliminate that monster before it reaches the city, so return the 'kill_monster' count
            if time[distance] - distance <= 0:
                return kill_monster
            else:
                # Otherwise, increment the 'kill_monster' count as you can eliminate the current monster
                kill_monster += 1
        
        # Return the 'kill_monster' count as the maximum number of monsters you can eliminate before losing
        return kill_monster
