class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        # Check if n is equal to 1 or n divided by 2 is equal to 1
        # This is to handle the case when n is a power of two (e.g., 1, 2, 4, 8, ...)
        if n / 2 == 1 or n == 1:
            return True

        # If n is greater than 2 and divisible by 2,
        # recursively call isPowerOfTwo with n/2
        if n > 2:
            return self.isPowerOfTwo(n/2)
        else:
            # If n is not a power of two, return False
            return False
