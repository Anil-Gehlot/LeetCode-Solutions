class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        # Check if n is non-positive, in which case it's not a power of three
        if n <= 0:
            return False
        
        # Calculate the logarithm of n with base 3
        log_value = math.log10(n)/ math.log10(3)
        
        # Check if the result is an integer, indicating that n is a power of three
        return log_value == int(log_value)
        