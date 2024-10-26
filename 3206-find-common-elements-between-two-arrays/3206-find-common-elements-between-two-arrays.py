class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [0, 0]

        for num in nums1:
            if num in set(nums2):
                result[0] += 1
        for num in nums2:
            if num in set(nums1):
                result[1] += 1
        return result
        