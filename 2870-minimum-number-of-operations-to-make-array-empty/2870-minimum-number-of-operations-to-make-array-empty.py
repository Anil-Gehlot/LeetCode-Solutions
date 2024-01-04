class Solution:
    def minOperations(self, nums: List[int]) -> int:

        # Dictionary to store the frequency of each element
        frequency_map = Counter(nums)

        # Variable to store the minimum operations required
        minimum_operations_required = 0

        # Iterate over the values (frequencies) in the dictionary
        for value in frequency_map.values():
            
            # If any value is 1, it means there is an element occurring only once,
            # and it is not possible to group it with others, so return -1.
            if value == 1:
                return -1

            # Calculate the minimum operations required for each group
            minimum_operations_required += (value + 2) // 3

        # Return the total minimum operations required
        return minimum_operations_required