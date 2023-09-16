class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        # finding the index if target is present inside the nums
        for number in nums:
            if number == target:
                return nums.index(number)
            
        # finding a index where target shuold be placed
        for number in nums:
            if number > target:
                return nums.index(number)

        # target should be placed at the end   
        return len(nums)
        