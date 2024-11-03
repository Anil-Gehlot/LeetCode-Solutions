class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        for i in range(len(goal)):
            goal = goal[-1]+ goal[:-1] 
            if goal == s:
                return True
        return False