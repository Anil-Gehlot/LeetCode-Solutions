class Solution:
    def tribonacci(self, n: int) -> int:
        
        # Base cases
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        # Initialize variables
        prev = 0
        curr = 1
        next = 1

        # Main loop to calculate Tribonacci sequence
        while n > 2:
            temp = prev + curr + next

            prev = curr 
            curr = next 
            next = temp

            n = n - 1

        return next
