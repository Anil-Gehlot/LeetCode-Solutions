class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
        # Initialize counts for positive and negative integers
        positive_count = 0
        negative_count = 0

        # Iterate through the list of integers
        for num in nums:
            
            # Check if the number is positive
            if num > 0:
                positive_count += 1
                
            # Check if the number is negative
            elif num < 0:
                negative_count += 1
        
        # Return the maximum count between positive and negative integers
        return max(positive_count, negative_count)
