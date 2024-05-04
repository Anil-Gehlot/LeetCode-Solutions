class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        # Check if the length of the array is less than 3
        if len(arr) < 3:
            return False

        # Find the index of the maximum element, which is the peak of the mountain
        max_element_index = arr.index(max(arr))

        # Split the array into two parts: increasing part and decreasing part
        incr_arr = arr[:max_element_index]
        decr_arr = arr[max_element_index:]

        # If either the increasing or decreasing part is empty, or if the decreasing part has only one element,
        # it's not a valid mountain array
        if not incr_arr or not decr_arr or len(decr_arr) == 1:
            return False

        # Check if elements in the increasing part are strictly increasing
        for i in range(len(incr_arr) - 1):
            if incr_arr[i] >= incr_arr[i + 1]:
                return False

        # Check if elements in the decreasing part are strictly decreasing
        for i in range(len(decr_arr) - 1):
            if decr_arr[i] <= decr_arr[i + 1]:
                return False

        # If all conditions are satisfied, it's a valid mountain array
        return True
