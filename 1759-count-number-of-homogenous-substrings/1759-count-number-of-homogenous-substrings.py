class Solution:
    def countHomogenous(self, s: str) -> int:
        # Define the modulo constant to avoid magic numbers.
        modulo = 10**9 + 7

        # Initialize variables for the result and the length of the current homogenous substring.
        result = 0
        length = 0

        # Iterate through the input string 's'.
        for i in range(len(s)):
            # Check if the current character is the same as the previous one.
            if i > 0 and s[i] == s[i-1]:
                # If it is, increment the length of the current homogenous substring.
                length += 1
            else:
                # If it's not, start a new homogenous substring with a length of 1.
                length = 1

            # Update the result by adding the current length to it, and take the result modulo 'modulo'.
            result = (result + length) % modulo

        # Return the final result, which represents the total number of homogenous substrings.
        return result
