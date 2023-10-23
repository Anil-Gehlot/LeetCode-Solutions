class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Check if n is non-positive, in which case it's not a power of four
        if n <= 0:
            return False

        # Calculate the logarithm of n with base 4
        log_value = math.log10(n) / math.log10(4)

        # Check if the result is an integer, indicating that n is a power of four
        return log_value == int(log_value)

        