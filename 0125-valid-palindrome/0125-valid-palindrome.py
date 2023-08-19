class Solution:
    def isPalindrome(self, s: str) -> bool:

        # to hold the string
        str1 = ""

        # iterating over the string
        for i in s:
            # ord() is used to convert a character 
            if( ord(i) <= 90 and ord(i) >=65 ) or ( ord(i) <= 122 and ord(i) >= 97 ) or ( ord(i) <= 57 and ord(i) >= 48 ):

                # adding to the string
                str1 = str1 + i
        
        # comparing both string
        if str1.lower()==str1[::-1].lower():
            return True
        else:
            return False