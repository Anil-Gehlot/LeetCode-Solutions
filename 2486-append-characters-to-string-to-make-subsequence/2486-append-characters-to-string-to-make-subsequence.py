class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # Pointers for s and t
        i, j = 0, 0
        
        # Traverse s to find the longest prefix of t that is a subsequence of s
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j += 1
                i += 1
            else:
                i += 1
        
        # The number of characters to append is the remaining part of t
        return len(t) - j