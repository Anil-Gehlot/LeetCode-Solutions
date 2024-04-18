from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        
        # Initialize the maximum triplet value to 0
        max_triplet_value = 0
        
        # Iterate over all possible starting points i
        for i in range(len(nums) - 2):
            
            # Iterate over all possible middle points j
            for j in range(i + 1, len(nums) - 1):
                
                # Iterate over all possible ending points k
                for k in range(j + 1, len(nums)):
                   
                    # Calculate the value of the current triplet
                    current_triplet_value = (nums[i] - nums[j]) * nums[k]
                    
                    # Update the maximum triplet value if necessary
                    max_triplet_value = max(max_triplet_value, current_triplet_value)
        
        # Return the maximum triplet value found
        return max_triplet_value

                    