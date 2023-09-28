class Solution:
    def reverseWords(self, s: str) -> str:

        s1 = s.split()
        string = ''

        for i in range(len(s1)-1, -1, -1):

            string += s1[i].strip()
    
            if i == 0:
                pass
            else:
                string += " "

        return string
        