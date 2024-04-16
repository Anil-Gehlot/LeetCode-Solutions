class Solution:
    def isSubstringPresent(self, s: str) -> bool:

        # Reverse the input string
        s_reverse = s[::-1]
        
        # Iterate over each index of the string up to the second-to-last index
        for i in range(len(s) - 1):
            
            # Extract a substring of length 2 starting from the current index i
            temp = s[i] + s[i+1]
            
            # Check if the substring exists in the reversed string
            if temp in s_reverse:
                return True  # If found, return True
            
        return False  # If no such substring is found, return False    