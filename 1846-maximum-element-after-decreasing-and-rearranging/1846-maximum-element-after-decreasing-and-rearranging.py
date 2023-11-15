class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:

        # Sort the input array in ascending order
        arr.sort()

        # Ensure the first element is 1
        if arr[0] != 1:
            arr[0] = 1

        # Adjust values to minimize differences between adjacent elements
        for i in range(1, len(arr)):
            # Calculate the absolute difference between the current and previous elements
            difference = abs(arr[i] - arr[i - 1])

            # Check if the difference is less than or equal to 1
            if difference <= 1:
                # If the difference is within the allowed range, no adjustment is needed
                pass
            else:
                # If the difference is greater than 1, adjust the value to minimize differences
                temp = arr.pop(i)
                arr.insert(i, temp - difference + 1)

        # Return the maximum element in the modified array
        return arr[-1]
