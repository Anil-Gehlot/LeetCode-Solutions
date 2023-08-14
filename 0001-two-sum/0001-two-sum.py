class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # to hold the index value
        list1 = []

        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if (nums[i]+nums[j]==target):
                    list1.append(i)
                    list1.append(j)

        return list1
