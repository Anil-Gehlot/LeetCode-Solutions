class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        
        # Initialize the result variable to 0.
        ans = 0
        
        # Iterate till 'n' becomes zero
        while n:
            
            # XOR operation the current value of 'ans' with 'n'
            ans ^= n
            
            # Right shift 'n' by 1 position
            n >>= 1
        
        # Return the final result
        return ans

        