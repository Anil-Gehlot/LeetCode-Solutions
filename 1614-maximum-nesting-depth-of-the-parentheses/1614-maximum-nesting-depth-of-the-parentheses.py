class Solution:
    def maxDepth(self, s: str) -> int:

        # Initialize variables to keep track of the max_depth and current bracket count
        max_depth = 0
        current_depth = 0

        # Iterate through each character in the string
        for char in s:
            
            if char == "(":
                
                # Increment bracket count when an open parenthesis is encountered
                current_depth += 1
                
                # Update the max_depth if the current bracket count exceeds the current max_depth
                if current_depth > max_depth:
                    max_depth = current_depth

            elif char == ")":
                
                # Decrement bracket count when a closing parenthesis is encountered
                current_depth -= 1

        # Return the final max_depth, which represents the maximum nesting depth
        return max_depth
