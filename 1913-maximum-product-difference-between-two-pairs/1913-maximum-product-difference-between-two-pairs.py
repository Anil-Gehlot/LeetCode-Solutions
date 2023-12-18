class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        
        # function to sort the array.
        def sortArray(arr):
            
            # Base case: if the array has 0 or 1 elements, it is already sorted
            if len(arr) <= 1:
                return arr
            
            else:
                # Choose the pivot as the first element of the array
                pivot = arr[0]

                # Create a list of elements less than or equal to the pivot
                less = [x for x in arr[1:] if x <= pivot]

                # Create a list of elements greater than the pivot
                greater = [x for x in arr[1:] if x > pivot]

                # Recursively sort the "less" and "greater" subarrays
                return sortArray(less) + [pivot] + sortArray(greater)
            
        # sorting the array nums
        nums = sortArray(nums)
        
        # applying the formula and finding the result : (a * b) - (c * d)
        result = ( nums[-1] * nums[-2] ) - ( nums[0] * nums[1] )
        
        # return the result 
        return result