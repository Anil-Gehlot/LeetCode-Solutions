class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        

        def sort_key(job):
            return job[1]  # Sort jobs by end time
        
        jobs = sorted(zip(startTime, endTime, profit), key=sort_key)
        
        dp = [(0, 0)]  # dp[i] represents the maximum profit until the ith job, along with the end time
        
        for start, end, p in jobs:
            idx = bisect_right(dp, (start, float('inf'))) - 1  # Find the latest job that finishes before the current job starts
            
            curr_profit = dp[idx][1] + p
            max_profit_until_now = max(curr_profit, dp[-1][1])
            
            dp.append((end, max_profit_until_now))
        
        return dp[-1][1]
