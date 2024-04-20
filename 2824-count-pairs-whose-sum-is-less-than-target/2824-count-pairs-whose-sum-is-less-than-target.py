class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
        # Initialize count to store the number of pairs
        count = 0
        
        # Iterate over each pair of indices (i, j) in the array
        for i in range(len(nums)):
            
            for j in range(i + 1, len(nums)):
                
                # Check if the sum of the pair (nums[i], nums[j]) is less than the target
                if nums[i] + nums[j] < target:
                    
                    # If the condition is met, increment the count
                    count += 1
        
        # Return the total count of pairs satisfying the condition
        return count
