class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        nums1 = []

        for i in nums:
            if i%2 == 0:
                nums1.insert(0, i)
            else:
                nums1.append(i)

        return nums1
        