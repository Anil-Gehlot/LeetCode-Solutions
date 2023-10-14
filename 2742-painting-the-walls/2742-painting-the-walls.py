class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        #memoization
        W = len(cost)

        @cache
        def dp(i, walls):
            if walls >= W:
                return 0
            if i == W:
                return inf
            
            return min(cost[i] + dp(i + 1, walls + 1 + time[i]), dp(i + 1, walls))
        return dp(0, 0)

        # bottom up
        C = len(cost)
        dp = [[0 for _ in range(C + 1)] for _ in range(C + 1)]

        for i in range(C):
            dp[C][i] = float('inf')

        for row in range(C - 1, -1, -1):
            for col in range(C - 1, -1, -1):
                painter = cost[row] +( dp[row + 1][col + time[row] + 1] if col + time[row] + 1 < len(dp[0]) else 0)
                dp[row][col] = min(dp[row+1][col], painter)
        return dp[0][0]

        # space optimized
        C = len(cost)
        dp = [inf]* C  + [0]
        
        for row in range(C - 1, -1, -1):
            new_dp = [0] * (C + 1)
            for col in range(C - 1, -1, -1):
                painter = cost[row] +( dp[col + time[row] + 1] if col + time[row] < C else 0)
                new_dp[col] = min(dp[col], painter)
            dp = new_dp
        return dp[0]

       
      #time O(n^2)
      #space O(n)