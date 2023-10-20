class Solution:
    def countAsterisks(self, s: str) -> int:
        
        # Initialize variables to keep track of vertical bars and asterisks count.
        vertical_bar = 0
        string_count = 0

        # Loop through each character in the input string.
        for letter in s:
            
            # If the current character is a vertical bar, increment the count.
            if letter == "|":
                vertical_bar += 1
            
            # If the current character is an asterisk and the number of vertical bars is even,
            # increment the count of asterisks.
            if letter == "*" and vertical_bar % 2 == 0:
                string_count += 1

        # Return the count of asterisks that meet the specified condition.
        return string_count
