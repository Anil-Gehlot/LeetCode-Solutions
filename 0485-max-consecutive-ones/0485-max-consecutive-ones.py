class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Initialize variables to keep track of the maximum consecutive count and the current count.
        max_count = 0
        count = 0

        # Iterate through the elements of the binary array 'nums'.
        for number in range(len(nums)):
            # Check if the current element is equal to 1 (consecutive 1's).
            if nums[number] == 1:
                # If it is, increment the current count of consecutive 1's.
                count += 1
            else:
                # If the current element is not 1 (i.e., 0 is encountered),
                # compare the 'count' to the 'max_count' and update 'max_count' if needed.
                if count > max_count:
                    max_count = count
                # Reset the current count to 0, as the consecutive sequence is broken.
                count = 0

        # Check the 'count' one last time after the loop, in case the maximum consecutive sequence
        # extends to the end of the binary array.
        if count > max_count:
            max_count = count

        # Return the 'max_count', which represents the maximum consecutive 1's found in the binary array.
        return max_count
