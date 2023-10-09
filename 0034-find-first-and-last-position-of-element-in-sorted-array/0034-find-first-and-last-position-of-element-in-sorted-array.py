class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Initialize a list to store the indices of occurrences of the target
        final_list = []

        # Search for the leftmost occurrence of the target
        for index in range(0, len(nums)):
            if nums[index] == target:
                final_list.append(index)  # Append the index to the final list
                break  # Stop the loop since we found the leftmost occurrence
        else:
            final_list.append(-1)  # If target not found, append -1

        # Search for the rightmost occurrence of the target
        for index in range(len(nums) - 1, -1, -1):
            if nums[index] == target:
                final_list.append(index)  # Append the index to the final list
                break  # Stop the loop since we found the rightmost occurrence
        else:
            final_list.append(-1)  # If target not found, append -1

        return final_list  # Return the list of leftmost and rightmost occurrences
