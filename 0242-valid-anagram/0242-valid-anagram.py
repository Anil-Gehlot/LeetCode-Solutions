class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # check if length of s and t is mismatch, return False.
        if len(s) != len(t):
            return False

        # empty dictionaries to count occurrences of each character in string s and t.
        s_count = dict()
        t_count = dict()

        # iterating through each character of s and adding them in a dictionary with their count.
        for char in s:
            if char in s_count:
                s_count[char] += 1
            elif char not in s_count:
                s_count[char] = 1

        # iterating through each character of t and adding them in a dictionary with their count.
        for char in t:
            if char in t_count:
                t_count[char] += 1
            elif char not in t_count:
                t_count[char] = 1
        
        # compare dictionaries and returning result.
        return s_count == t_count 

        