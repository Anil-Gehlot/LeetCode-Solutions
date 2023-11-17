class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        # Sort the array in ascending order.
        nums.sort()
        
        # Initialize start and end indices.
        start = 0
        end = len(nums)-1
        
        # Initialize the maximum pair sum.
        max_sum = 0 
        
        # Use a while loop to iterate until start is less than end.
        while (start < end ):
            
            # Calculate the pair sum of the current pair (nums[start], nums[end]).
            result = nums[start] + nums[end]
            
            #  Update start and end indices.
            start += 1
            end -= 1
            
            # If the calculated pair sum is greater than the current max_sum, update max_sum.
            if result > max_sum :
                max_sum = result
                
        # Return the final max_sum.        
        return max_sum
        