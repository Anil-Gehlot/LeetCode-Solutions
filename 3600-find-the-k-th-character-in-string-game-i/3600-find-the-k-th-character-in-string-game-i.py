class Solution:
    def helper(self, k, s='a'):
        if len(s) >= k:
            print(s)
            return s[k-1]
            
        for i in range(len(s)):
            s += chr(ord(s[i])+1)

        return self.helper(k, s)
        

    def kthCharacter(self, k: int) -> str:
        return self.helper( k)
        