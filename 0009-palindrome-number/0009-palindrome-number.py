class Solution:
    def isPalindrome(self, x: int) -> bool:

        if (x<0):
            return False
        
        num = x
        rev = 0
      
        while( num != 0):
            l_digit = num%10
            rev = ( rev*10 ) + l_digit
            num = num // 10
        
        if (rev == x):
            return True
        else:
            return False
          
