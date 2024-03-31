from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        # Initialize arr1 with the first element of nums
        arr1 = [nums[0]]
        # Initialize arr2 with the second element of nums
        arr2 = [nums[1]]

        # Iterate over the remaining elements of nums starting from index 2
        for i in range(2, len(nums)):
            # If the last element of arr1 is greater than the last element of arr2
            if arr1[-1] > arr2[-1]:
                # Append the current element of nums to arr1
                arr1.append(nums[i])
            else:
                # Append the current element of nums to arr2
                arr2.append(nums[i])
        
        # Return the concatenation of arr1 and arr2
        return arr1 + arr2
