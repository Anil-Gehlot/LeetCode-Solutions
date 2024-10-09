class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        stack =[]

        for p in s:
            if len(stack) == 0:
                stack.append(p)
            elif p == ")" and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(p)
        return len(stack)