
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        # Initialize a dictionary to store elements from the same diagonal
        diagonal_dict = {}

        # Iterate through the rows of the 2D array
        for row_index in range(len(nums)):
            
            # Iterate through the elements in the current row
            for col_index in range(len(nums[row_index])):
                
                # Calculate the key for the current diagonal
                diagonal_key = row_index + col_index
                
                # Check if the key exists in the dictionary
                if diagonal_key in diagonal_dict:
                    
                    # If the key exists, append the element to the corresponding list
                    diagonal_dict[diagonal_key].append(nums[row_index][col_index])
                    
                else:
                    # If the key doesn't exist, create a new list with the element
                    diagonal_dict[diagonal_key] = [nums[row_index][col_index]]

        # Initialize a list to store the final result
        final_list = []

        # Iterate through the values (lists of elements from the same diagonal) in the dictionary
        for diagonal_elements in diagonal_dict.values():
            
            # Iterate through the elements in reverse order and append them to the final list
            for reversed_index in range(len(diagonal_elements) - 1, -1, -1):
                
                final_list.append(diagonal_elements[reversed_index])


        # Return the final result
        return final_list
