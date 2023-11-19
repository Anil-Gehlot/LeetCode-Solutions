class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        
        # Sort the array in ascending order.
        nums.sort() 
        
        # Initialize a variable to count the total number of operations.
        operations_count = 0  

        # Iterate through the array from the end to the beginning.
        for max_index in range(len(nums)-1, 0, -1):
            
            # Check if the current element is greater than the previous one.
            if nums[max_index] > nums[max_index - 1]:
                
                # Increment the count by the difference in indices.
                operations_count += len(nums) - max_index

        # Return total np. of operation
        return operations_count
