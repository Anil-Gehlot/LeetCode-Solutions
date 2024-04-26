class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        
        # Find the maximum element in the array
        max_num = max(nums)

        # Initialize the sum variable to keep track of the total score
        sum = 0

        # Perform the operation k times
        for i in range(k):
            
            sum += max_num  # Increase the sum by the maximum element
            max_num += 1  # Increment the maximum element by 1 for the next iteration

        # Return the final sum
        return sum
