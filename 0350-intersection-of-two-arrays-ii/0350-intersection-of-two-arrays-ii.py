class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Create an empty list to store the intersection of nums1 and nums2.
        final_list = []
        
        # Iterate through each number in nums1.
        for number in nums1:
            # Check if the current number is also present in nums2.
            if number in nums2:
                # If the number is found in nums2, add it to the final_list.
                final_list.append(number)
                # Remove the number from nums2 to avoid duplicate entries.
                nums2.remove(number)
        
        # Return the final_list containing the intersection of nums1 and nums2.
        return final_list

        