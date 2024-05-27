class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        for x in range(n + 1):
            # Count the number of elements greater than or equal to x
            count = 0
            for num in nums:
                if num >= x:
                    count += 1
                    
            
            # Check if the count matches x
            if count == x:
                return x
        
        # If no such x is found, return -1
        return -1