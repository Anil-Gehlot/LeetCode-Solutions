class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        final_list = []
        
        for number in nums1:
            
            if number in nums2:
                final_list.append(number)
                nums2.remove(number)
                
        return final_list
            
        