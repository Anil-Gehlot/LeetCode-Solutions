from typing import List

class Solution:
    
    # Function to find the maximum digit in a number
    def max_digit(self, num: int) -> int:
        
        max_digit = 0
         
        # Iterate through each digit of the number and Update max_digit if current digit is greater
        while num > 0:
            last_digit = num % 10
            max_digit = max(max_digit, last_digit) 
            num //= 10  
        return max_digit

    # Main function to find the maximum sum of pairs with equal maximum digits
    def maxSum(self, nums: List[int]) -> int:
        
        max_sum = -1  
        
        # Iterate through pairs of numbers in the list
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                max_digit_i = self.max_digit(nums[i])  # Find the maximum digit of nums[i]
                max_digit_j = self.max_digit(nums[j])  # Find the maximum digit of nums[j]

                # If both numbers have equal maximum digits, update max_sum if necessary
                if max_digit_i == max_digit_j:
                    max_sum = max(max_sum, nums[i] + nums[j])

        return max_sum  # Return the maximum sum found
