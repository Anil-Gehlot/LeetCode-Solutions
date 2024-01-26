class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
 
        MOD = 10**9 + 7
        dp_prev = [[0] * n for _ in range(m)]
        dp_prev[startRow][startColumn] = 1
        result = 0

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for _ in range(maxMove):
            dp_curr = [[0] * n for _ in range(m)]

            for i in range(m):
                for j in range(n):
                    for dx, dy in directions:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < m and 0 <= nj < n:
                            dp_curr[i][j] = (dp_curr[i][j] + dp_prev[ni][nj]) % MOD
                        else:
                            result = (result + dp_prev[i][j]) % MOD

            dp_prev = dp_curr

        return result