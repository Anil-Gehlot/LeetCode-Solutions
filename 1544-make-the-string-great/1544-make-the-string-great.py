class Solution:
    def makeGood(self, s: str) -> str:
        
        # Initialize an empty list to store characters forming the resulting string
        result_chars = []

        # Iterate through each character in the input string
        for char in s:
            
            # Check if the result_chars list is not empty
            if result_chars:
                
                # Compare the current character with the last character in result_chars
                # using their ASCII values to check for case-insensitive matches
                if abs(ord(result_chars[-1]) - ord(char)) == 32:
                    # If the characters are case-insensitive matches, remove the last character
                    # from result_chars
                    result_chars.pop()
                    
                else:
                    # If the characters are not case-insensitive matches, append the current character
                    # to result_chars
                    result_chars.append(char)
            else:
                # If result_chars is empty, append the current character to it
                result_chars.append(char)

        # Join the characters in result_chars to form the resulting string
        return "".join(result_chars)
