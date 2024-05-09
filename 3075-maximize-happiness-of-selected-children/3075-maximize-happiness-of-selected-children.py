class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
        # Sort the happiness array in descending order
        happiness.sort(reverse=True)

        # variable to store the maximum happiness sum
        max_happiness = 0
        
        # Iterate through the first k elements of the sorted happiness array
        for i in range(k):
            
            # Calculate the adjusted happiness value for the current child
            happiness_value = happiness[i] - i
            
            # If the adjusted happiness value is non-negative, add it to max_happiness
            if happiness_value >= 0:
                max_happiness += happiness_value
        
        # Return the maximum happiness sum
        return max_happiness
 