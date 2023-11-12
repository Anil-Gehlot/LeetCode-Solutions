class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        # Initialize the minimum variable to None
        minimum = None
        
        # Check which input is greater and assign it to the minimum variable
        if a > b:
            minimum = a
        else:
            minimum = b
            
        # Initialize a counter variable to count common factors
        counter = 0
            
        # Iterate through divisors from 1 to the minimum of a and b
        for divisor in range(1, minimum + 1):
            # Check if divisor is a factor of both a and b
            if (a % divisor == 0 and b % divisor == 0):
                # Increment the counter if it is a common factor
                counter += 1
        
        # Return the final count of common factors
        return counter
