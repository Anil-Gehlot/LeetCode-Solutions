class Solution:
    def romanToInt(self, s: str) -> int:

        # dictionary to fetch the integer value
        values ={
            'I':1,
            'V':5,
            'X':10,
            'L':50, 
            'C':100,
            'D':500,
            'M':1000
        }

        # replacing the of roman like 4, 9, 40, 90, 400 and 900
        s = s.replace("IV", "IIII")
        s = s.replace("IX", "VIIII")
        s = s.replace("XL", "XXXX")
        s = s.replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC")
        s = s.replace("CM", "DCCCC")

        # contains the integer value of Roman
        sum = 0
        
        # traversing the given roman numbers
        for letter in s:
            
            # adding letters integer value to sum
            sum += values[letter]
        
        # returning sum  
        return sum
