class Solution:
    def arrangeCoins(self, n: int) -> int:
        x = 1
        while n >=x :
            n = n-x
            x += 1

        return x-1
        