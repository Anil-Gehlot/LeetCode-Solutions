class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        
        # Get the length of the nums list
        n = len(nums)
        
        # Initialize a variable to store the sum of squares of special elements
        special_sum = 0
        
        # Iterate over numbers from 1 to n (inclusive)
        for i in range(1, n + 1):
            
            # Check if i divides n evenly (i is a divisor of n)
            if n % i == 0:
                
                # If i divides n evenly, it means nums[i-1] is a special element,
                # so add its square to the special_sum
                special_sum += nums[i - 1] * nums[i - 1]
        
        # Return the sum of squares of special elements
        return special_sum
