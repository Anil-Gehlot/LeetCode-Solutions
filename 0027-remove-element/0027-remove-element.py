class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        index = 0
        
        while index < len(nums) :
            if nums[index] == val :
                nums.pop(index)
            else:
                index += 1
        return len(nums)