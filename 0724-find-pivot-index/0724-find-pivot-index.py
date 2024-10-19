class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = [nums[0]]
        right_sum = [nums[-1]]

        for i in range(1, len(nums)):
            left_sum.append(left_sum[-1]+nums[i])

        for j in range(len(nums)-2, -1,-1):
            right_sum.insert(0, right_sum[0]+nums[j])

        for i in range(len(nums)):
            if right_sum[i] == left_sum[i]:
                return i
        else:
            return -1

        