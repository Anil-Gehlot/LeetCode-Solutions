class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        
        # Convert integer to string to access its digits
        x_str = str(x)
        
        # Calculate the sum of digits
        digit_sum = sum(int(digit) for digit in x_str)
        
        # Check if x is divisible by the sum of its digits
        if x % digit_sum == 0:
            return digit_sum
        else:
            return -1