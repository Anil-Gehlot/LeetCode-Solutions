class Solution:
    def fibonacci(self, n, dp):
        if n == 1 or n == 0:
            return n
        
        if dp[n] != -1:
            return dp[n]
        
        dp[n] = self.fibonacci(n-1, dp) + self.fibonacci(n-2, dp)
        return dp[n]

    def fib(self, n: int) -> int:
        dp = [-1] * (n+1)
        print(dp)
        return self.fibonacci(n, dp)

        

        