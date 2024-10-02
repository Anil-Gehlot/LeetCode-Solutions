class Solution:
    def recursive_bs(self, nums, target, start, end):
        if start > end :
            return -1
        
        mid = (start+end)//2
        print(mid)
        if nums[mid] == target:
            return mid
        
        if target < nums[mid]:
            return self.recursive_bs(nums, target, start, mid-1)
        else:
            return self.recursive_bs( nums, target, mid+1, end)
    def search(self, nums: List[int], target: int) -> int:
        return self.recursive_bs(nums, target, 0, len(nums)-1)
        