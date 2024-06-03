class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        # Initialize two pointers, i for traversing t and j for traversing s
        i, j = 0, 0
        
        # Loop through t until we reach the end of t or the end of s
        while i < len(t) and j < len(s):
            
            # If characters at t[i] and s[j] match
            if t[i] == s[j]:
                
                # Move to the next character in both strings
                i += 1
                j += 1
            else:
                # Otherwise, just move to the next character in t
                i += 1
        
        # If j has reached the end of s, all characters of s are found in t in sequence
        return j == len(s)
