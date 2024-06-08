class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 2
        
        while j < len(nums):
            if nums[i] == nums[j]:
                nums.pop(j)
            else:
                i += 1
                j += 1
        return len(nums)
        