class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        # dp[i] := max sum of non-empty subsequence in nums[0..i]
        dp = [0] * len(nums)
        # dq stores dp[i - k], dp[i - k + 1], ..., dp[i - 1] whose values are > 0
        # in decreasing order.
        dq = collections.deque()

        for i, num in enumerate(nums):
            if dq:
                # If dq is not empty, calculate the maximum sum by considering
                # the current number 'num' and the maximum sum from the previous
                # subsequence stored at dq[0].
                dp[i] = max(dq[0], 0) + num
            else:
                # If dq is empty, set dp[i] to the current number 'num'.
                dp[i] = num
            while dq and dq[-1] < dp[i]:
                # Remove elements from the back of the deque that are smaller than
                # the current dp[i] value, ensuring that the deque stores values in
                # decreasing order.
                dq.pop()
            dq.append(dp[i])
            if i >= k and dp[i - k] == dq[0]:
                # If the current index is greater than or equal to k, and the
                # maximum value from the last subsequence (dp[i - k]) is equal to
                # the maximum value stored at the front of dq, remove the front
                # value to maintain a window of size 'k'.
                dq.popleft()

        return max(dp)
