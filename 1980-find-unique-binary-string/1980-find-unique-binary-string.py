class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

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