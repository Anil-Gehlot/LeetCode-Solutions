from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        
        # Get the length of the binary strings in the array
        n = len(nums)

        # Create a binary string of all ones and all zeros with length n
        all_ones = "1" * n
        all_zeros = "0" * n

        # Check if the binary string of all ones is not in nums, return it
        if all_ones not in nums:
            return all_ones

        # Check if the binary string of all zeros is not in nums, return it
        if all_zeros not in nums:
            return all_zeros
        
        # Iterate through each binary string in nums
        for binary_str in nums:
            # Check if the reverse of the current string is not in nums, return the reversed string
            if binary_str[::-1] not in nums:
                return binary_str[::-1]
        
        # last case: If none of the above conditions are met, return "10"
        return "10"

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''

        # Handling the case where the array has only one element
        if len(nums)==1 and "0" not in nums:
            return "0"
        if len(nums)==1 and "1" not in nums:
            return "1"

        n = len(nums)

         # Initialize a binary string with all "1"
        bin_num = "1"*n
        
        # Check if bin_num is not in nums, return it
        if bin_num not in nums:
            return bin_num
        
        # Iterate through strings in nums and return the first one not present
        for i in nums:
            if i[::-1] not in nums:
                return i[::-1]
        
        # last case 
        return "10"
        
        '''