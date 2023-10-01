class Solution:
    def reverseWords(self, s: str) -> str:

        # splittin each worh of given string    
        s = s.split()

        # variable to hold reversed string
        final_string = ''

        # adding reveresed string to variable
        for i in range(len(s)):
            final_string += s[i][::-1]

            #adding space in it is not last word
            if i != len(s)-1:
                final_string += " "

        #returning the reversed string
        return final_string

        