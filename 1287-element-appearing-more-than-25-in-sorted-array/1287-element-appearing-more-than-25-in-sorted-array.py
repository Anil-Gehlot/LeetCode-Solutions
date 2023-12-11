
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

        # A dictionary to store the count of occurrences for each unique element
        count_dict = {}

        # Count occurrences of each unique element in the array
        for num in arr:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1

        # Find the key with the maximum count
        max_count = 0
        max_count_key = 0

        for key, count in count_dict.items():
            if count > max_count:
                max_count = count
                max_count_key = key 

        # Return the key with the maximum count
        return max_count_key
