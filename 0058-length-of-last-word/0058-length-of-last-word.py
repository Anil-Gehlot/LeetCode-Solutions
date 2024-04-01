class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Removes leading and trailing spaces
        s = s.strip()
        
        # Splits the string by spaces
        s = s.split()
        
        # Returns the length of the last word
        return len(s[-1])
        