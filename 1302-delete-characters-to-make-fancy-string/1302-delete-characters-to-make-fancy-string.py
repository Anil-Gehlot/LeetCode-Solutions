class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []

        for char in s:
            if len(result) >= 2 and result[-1] == char and result[-2] == char:
                continue
            result.append(char)
        
        return "".join(result)