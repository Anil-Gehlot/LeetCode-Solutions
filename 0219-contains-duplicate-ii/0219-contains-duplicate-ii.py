class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Create a dictionary to store the indices of each unique number in the input list.
        dict = {}
        
        # Iterate through the list 'nums'.
        for i in range(len(nums)):
            # If 'nums[i]' is not in the dictionary keys, create a new entry with the number as the key
            # and a list containing the current index 'i' as the value.
            if nums[i] not in dict.keys():
                dict[nums[i]] = [i]
            # If 'nums[i]' is already a key in the dictionary, append the current index 'i' to the
            # list associated with that key.
            elif nums[i] in dict.keys():
                dict[nums[i]].append(i)
                
        # Print the dictionary for debugging purposes.
        print(dict)
        
        # Iterate through the values (which are lists of indices) in the dictionary.
        for i in dict.values():
            # If the length of the list is 2, check if the difference between the two indices is less than or equal to 'k'.
            if len(i) == 2:
                if i[1] - i[0] <= k:
                    return True
            # If the length of the list is greater than 2, compare each pair of indices to check if the difference is less than or equal to 'k'.
            if len(i) > 2:
                for x in range(len(i) - 1):
                    for y in range(x + 1, len(i)):
                        if i[y] - i[x] <= k:
                            return True
                
        # If no duplicates with a difference of at most 'k' were found, return False.
        return False
