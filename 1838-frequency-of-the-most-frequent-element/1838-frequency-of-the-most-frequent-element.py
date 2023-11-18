
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        # Sort the array to simplify finding the maximum frequency.
        nums.sort()

        # Initialize variables to keep track of the maximum frequency,
        # the left index of the current subarray, and the sum of elements in the current subarray.
        max_freq = 0
        left = 0
        curr_sum = 0

        # Iterate over the array using .
        for right in range(len(nums)):
            curr_sum += nums[right]  # Include the current element in the subarray.

            # Check if the current subarray can be transformed to have equal elements
            # using at most k operations. If not, move the left pointer to shrink the subarray.
            while (right - left + 1) * nums[right] - curr_sum > k:
                
                curr_sum -= nums[left]  # Exclude the leftmost element from the subarray.
                left += 1

            # Update the maximum frequency with the size of the current subarray.
            if max_freq < right - left + 1:
                max_freq = right - left + 1
                

        # Return the maximum frequency found.
        return max_freq