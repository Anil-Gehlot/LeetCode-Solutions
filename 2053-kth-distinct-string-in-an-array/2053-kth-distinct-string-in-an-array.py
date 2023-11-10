
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # Initialize an empty list to store unique elements
        unique_element = []

        # Iterate through the indices of the array
        for string in range(len(arr)):
            # Pop the element at the current index
            temp = arr.pop(string)

            # Check if the popped element is not in the modified array
            if temp not in arr:
                # If not, add it to the list of unique elements
                unique_element.append(temp)
                # Insert an empty string at the current index to maintain array length
                arr.insert(string, '')
            else:
                # If the popped element is already in the modified array, insert it back
                arr.insert(string, temp)

        # Check if there are enough unique elements to return the kth distinct element
        if len(unique_element) >= k:
            return unique_element[k-1]

        # If there are not enough unique elements, return an empty string
        return ''