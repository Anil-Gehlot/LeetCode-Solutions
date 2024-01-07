class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        # Length of array nums
        n = len(nums)
        
        # Initialize dp as dictionary till length of array nums
        dp = [defaultdict(int) for _ in range(n)]
        
        # Variable to count arithematic subsequences of nums
        count = 0

        # Iterate through the array starting from the second element
        for i in range(1, n):
            
            # Iterate through i starting from index where j < i
            for j in range(i):
                
                # Calculate the common difference
                d = nums[i] - nums[j]
                
                # Update the count of arithmetic slices ending at index i with common difference d
                dp[i][d] += dp[j][d] + 1
                
                # Accumulate the count of arithmetic slices globally
                count += dp[j][d]
        
        # Return the total count of arithmetic slices
        return count