class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # to remove spaces fromt the begining and from the last of string
        str1 = s.strip()

        # to split each word separated by space
        str_list = str1.split()

        # returning the last word
        return len(str_list[-1])