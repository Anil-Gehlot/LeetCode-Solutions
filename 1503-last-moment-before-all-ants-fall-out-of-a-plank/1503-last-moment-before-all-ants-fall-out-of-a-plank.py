class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        
        # in this solution just forget about the collision, just remember thing that:
        # 1. what is the max time is taken by ants while moving from left to right till the last ant fall out of the plan.
        # 2. what is the max time is taken by ants while moving from right to left till the last ant fall out of the plan.
        
        
        # Initialize left_max to 0 to track the maximum position of ants moving from left to right.
        left_max = 0
        
        # Iterate through ants moving from left to right.
        # Update left_max to the maximum position of ants on the left side.
        for ant in left:
            if ant > left_max:
                left_max = ant 

        # Initialize right_max to n, which represents the maximum position of ants moving from right to left.
        right_max = n
        
        # Iterate through ants moving from right to left.
        # Update right_max to the minimum position of ants on the right side (by subtracting from n).
        for ant in right:
            if ant < right_max:
                right_max = ant
                
        # Calculate the time taken by ants moving from right to left as the difference from n.
        right_max = n - right_max

        # Compare left_max (time taken by ants moving from left to right) and right_max
        # (time taken by ants moving from right to left).
        # Return the greater of the two, as that represents the last moment when an ant falls off the plank.
        if left_max > right_max:
            return left_max
        else:
            return right_max
