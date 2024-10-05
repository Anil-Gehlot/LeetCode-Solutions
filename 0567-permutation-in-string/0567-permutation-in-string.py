class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if all char if s1 not in s2, then return False.
        for char in s1:
            if char not in s2:
                return False

        s1 = "".join(sorted(s1))
        s1_length = len(s1)

        for i in range(len(s2)-s1_length+1):
            substr = s2[i: i+s1_length]

            if ''.join(sorted(substr)) == s1:
                return True

        return False 