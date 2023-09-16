class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        for number in nums:
            if number == target:
                return nums.index(number)
            
        
        for number in nums:
            if number > target:
                return nums.index(number)
              
        return len(nums)
        