class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        if k == 0:
            return 0

        # Initialize a 3D array to store the number of ways
        # dp[i][c][j] represents the number of ways to have an array of length i
        # with c elements used to obtain a maximum of j
        dp = [[[0] * (m + 1) for _ in range(k + 1)] for _ in range(n + 1)]
        mod = 10**9 + 7

        # Base case: there's only one way to have an array of length 1
        # with each maximum value from 1 to m
        for i in range(1, m + 1):
            dp[1][1][i] = 1

        # Fill the dp table based on the given conditions
        for i in range(2, n + 1):
            for c in range(1, min(k + 1, i + 1)):
                for j in range(1, m + 1):
                    # The number of ways to construct an array of length i with
                    # c elements used to obtain a maximum of j is calculated here
                    dp[i][c][j] = dp[i - 1][c][j] * j
                    for j0 in range(1, j):
                        dp[i][c][j] += dp[i - 1][c - 1][j0]
                        dp[i][c][j] %= mod

        # Calculate the total number of ways to construct the array
        ans = 0
        for i in range(1, m + 1):
            ans += dp[n][k][i]
            ans %= mod

        return ans
