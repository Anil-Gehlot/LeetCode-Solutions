class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        nums1 = []
        for i in range(0, len(nums)-1):
    
            for j in range(i+1, len(nums)):
        
                if nums[i] == nums[j]:
                    nums1.append( [i,j] )

        return len(nums1)
        