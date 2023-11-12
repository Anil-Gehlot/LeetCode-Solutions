from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Initialize an empty dictionary to store occurrences of each number
        occurrences_dict = {}
        
        # Iterate through the numbers in the array
        for number in arr:
            # Check if the number is already in the dictionary
            if number in occurrences_dict:
                # Increment the count if the number is already present
                occurrences_dict[number] += 1
            else:
                # Add the number to the dictionary with a count of 1 if it's not present
                occurrences_dict[number] = 1
        
        # Extract the list of occurrences from the dictionary
        occurrence_list = occurrences_dict.values()
        
        # Convert the list of occurrences to a set to get unique counts
        occurrence_set = set(occurrence_list)
        
        # Check if the length of the list of occurrences is the same as the length of the set
        if len(occurrence_list) == len(occurrence_set):
            return True  # The number of occurrences is unique
        
        return False  # The number of occurrences is not unique
