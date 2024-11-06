class Solution:
    def isBalanced(self, num: str) -> bool:
        total_sum = 0
        for i in range(0, len(num), 2):
            total_sum += int(num[i])
            if i+1 < len(num):
                total_sum -= int(num[i+1])
        return total_sum == 0