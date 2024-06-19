class Solution:
    def solveUsingRecursion(self, nums, n, dp):
        if n < 0:
            return 0
        if n == 0:
            return nums[0]

        if dp[n] != -1:
            return dp[n]

        include = self.solveUsingRecursion(nums, n-2, dp) + nums[n]
        exclude = self.solveUsingRecursion(nums, n-1, dp)

        dp[n] = max(include, exclude)
        return max(include, exclude)

    def rob(self, nums: List[int]) -> int:
        n = len(nums)-1
        dp = [-1] * (n+1)
        return self.solveUsingRecursion(nums, n, dp)

        