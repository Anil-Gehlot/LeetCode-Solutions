class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        index = 0

        while index < len(s):
            if len(stack) == 0:
                stack.append(s[index])
                index += 1
            elif stack[-1] == "A" and s[index] == "B" or stack[-1] == "C" and s[index] == "D":
                stack.pop()
                index += 1
            else:
                stack.append(s[index])
                index += 1
        return len(stack)
        