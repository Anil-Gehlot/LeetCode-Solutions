class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        
        # Initialize variables to store the sums
        num1 = 0  # Sum of numbers not divisible by m
        num2 = 0  # Sum of numbers divisible by m
        
        # Iterate through numbers from 1 to n
        for num in range(1, n+1):
            
            # If the number is divisible by m
            if num % m == 0:
                
                # Add it to the sum of numbers divisible by m
                num2 += num
            else:
                
                # Otherwise, add it to the sum of numbers not divisible by m
                num1 += num
        
        # Return the difference between the sums
        return num1 - num2
