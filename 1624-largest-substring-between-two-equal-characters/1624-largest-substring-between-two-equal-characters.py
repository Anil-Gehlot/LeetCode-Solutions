class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        # Initialize the maximum length to -1
        max_length = -1

        # Iterate through the string
        for i in range(len(s)-1):
            
            for j in range(i+1, len(s)):
                
                # Check if characters at positions i and j are equal
                if s[i] == s[j]:
                    
                    # Calculate the length of the substring between the equal characters
                    diff = j - i - 1

                    # Update the maximum length if the current length is greater
                    if diff > max_length:
                        max_length = diff

        # Return the maximum length found, or -1 if no such substring exists
        return max_length
