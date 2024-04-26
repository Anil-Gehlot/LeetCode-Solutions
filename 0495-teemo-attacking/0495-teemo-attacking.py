class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:

        # Initialize variable to store total poisoned time
        total_poisoned_time = 0  

        # Iterate through the timeSeries array
        for i in range(len(timeSeries) - 1):

            # Calculate the gap between the current attack and the next attack
            time_gap = timeSeries[i + 1] - timeSeries[i]

            if time_gap > duration:
                total_poisoned_time += duration
            else:
                total_poisoned_time += time_gap
        
        # Add the duration of the last attack to the total poisoned time
        total_poisoned_time += duration

        # Return the total poisoned time
        return total_poisoned_time
