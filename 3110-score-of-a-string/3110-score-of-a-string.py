class Solution:
    def scoreOfString(self, s: str) -> int:
        
        # Initialize a variable to keep track of the total score
        sum = 0
        
        # Loop through the string up to the second last character
        for i in range(len(s)-1):
            
            # Calculate the absolute difference between the ASCII values of current and next characters
            diff = abs(ord(s[i]) - ord(s[i+1]))
            
            # Add the absolute difference to the total score
            sum += diff
            
        # Return the total score
        return sum
