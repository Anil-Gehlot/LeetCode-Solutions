class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        # sorting nums in ascending order
        nums.sort()
        
        # finding the duplicate
        duplicate = -1
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                duplicate = nums[i]
                break

        # finding the missing using a set for efficient membership test
        nums_set = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in nums_set:
                
                # return the result directly
                return [duplicate, i]