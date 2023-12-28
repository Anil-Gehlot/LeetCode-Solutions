class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        # Using a dictionary to store computed results to avoid redundant calculations
        cache = {}

        # Recursive function to calculate the optimal length of run-length encoding
        def count(i, k, prev, prev_cnt):

            # Check if the result for the current state is already in the cache
            if(i, k, prev, prev_cnt) in cache:
                return cache[(i, k, prev, prev_cnt)]

            # Base case: if no more characters to process, return 0
            if k < 0:
                return float("inf")

            # If there are negative deletions, return infinity (not a valid state)
            if i==len(s):
                return 0

            # If the current character is the same as the previous one, increase the count
            if s[i] == prev:
                incr = 1 if prev_cnt in [1, 9, 99] else 0
                # Recursively calculate the result without changing the current character
                res = incr + count(i+1, k, prev, prev_cnt+1)

            else:
                # Choose the minimum between two options:
                # 1. Delete the current character and recursively calculate the result
                # 2. Keep the current character and recursively calculate the result for the next character
                res = min( count(i+1, k-1, prev, prev_cnt), 1+count(i+1, k, s[i], 1) )
            
            # Store the result in the cache for future reference
            cache[(i, k, prev, prev_cnt) ] = res
            return res

        # Start the recursive calculation from the beginning of the string
        return count(0, k, "", 0)
