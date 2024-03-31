from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        # Find elements less than k
        less_than_k = [num for num in nums if num < k]
        
        # Return the count of elements less than k
        return len(less_than_k)
