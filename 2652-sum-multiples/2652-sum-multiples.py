class Solution:
    def sumOfMultiples(self, n: int) -> int:
        # Initialize a variable 'sum' to keep track of the sum of multiples
        sum = 0
        
        # Iterate through numbers from 1 to 'n' (inclusive)
        for number in range(1, n+1):
            # Check if the current number is a multiple of 3, 5, or 7
            if number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
                # If it's a multiple of any of the specified numbers, add it to the 'sum'
                sum += number
                
        # Return the final sum of multiples
        return sum
