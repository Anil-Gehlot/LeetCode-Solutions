class Solution:
    def minOperations(self, s: str) -> int:
        
        # Initialize a variable to count the cost of making the string "1010"
        cost10 = 0
        
        # Iterate over the characters of the string along with their indices
        for i, c in enumerate(s):
            
            # Check if the character needs to be changed to achieve "1010" pattern
            if int(c) == i % 2:
                cost10 += 1

        # Calculate the cost of making the string "0101"
        cost01 = len(s) - cost10

        # Return the minimum cost between the "1010" and "0101" patterns
        return min(cost10, cost01)