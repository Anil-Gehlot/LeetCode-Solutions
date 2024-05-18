class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)  # Initialize ans with the same length as nums
        for i in range(len(nums)):
            ans[i] = nums[nums[i]]  # Assign the value as per the rule
        return ans
   