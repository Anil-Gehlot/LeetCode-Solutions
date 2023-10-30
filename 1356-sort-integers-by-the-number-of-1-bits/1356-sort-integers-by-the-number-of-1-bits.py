class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # Define a custom sorting key using a lambda function.
        # This key is used by the sorted() function to determine the order of elements in the output list.
        sorting_key = lambda x: (bin(x).count('1'), x)
        
        # Sort the input list 'arr' using the sorting key.
        # Elements will be sorted first by the count of set bits (1s) in their binary representation,
        # and in case of a tie, by their original values.
        sorted_arr = sorted(arr, key=sorting_key)
        
        # Return the sorted list as the output.
        return sorted_arr
