class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        # Check if the lengths of s and goal are different
        if len(s) != len(goal):
            return False
        
        # Check if goal is a substring of s concatenated with itself
        return goal in (s + s)