class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        # empty list to store the equal numbers indexes.
        nums1 = []

        # outer loop to traverse all numbers excluding last.
        for i in range(0, len(nums)-1):
            
            # inner loop to traverse all numbers excluding last.
            for j in range(i+1, len(nums)):
                
                # comparing numbers and adding in nums1
                if nums[i] == nums[j]:
                    nums1.append( [i,j] )

        #returning the count of matched numbers
        return len(nums1)
        