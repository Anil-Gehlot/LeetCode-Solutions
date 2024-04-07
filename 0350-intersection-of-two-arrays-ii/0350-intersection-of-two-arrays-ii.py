class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        result = []

        for val in nums1 :
            if val in nums2:
                result.append(val)
                nums2.remove(val)
                
        return result


        