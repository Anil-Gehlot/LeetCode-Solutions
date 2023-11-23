class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
         # function to check if a given list can be rearranged into an arithmetic sequence or not.
        def check_arithmetic(subarray):
            
            # Sort the array in ascending order.
            subarray.sort()
            
            # Calculating the difference between the first two element.
            difference = subarray[0] - subarray[1]
            
            # Iterate through the array and check the difference for all is same or not.
            for i in range(len(subarray)-1  ):
                
                # If the difference is not same, return False.
                if subarray[i] - subarray[i+1] != difference:
                    return False

            # If the difference is same for all pairs, return True      
            return True

        # # Initialize an empty list to store the results for each subarray.
        final_list = []

        # Iterate through the subarray in  given ranges between left_index and right_index.
        for left_index, right_index in zip(l, r):
            
             # Extract the subarray by nums slicing.
            temp_array = nums[ left_index : right_index+1 ]
            
            # checking that the subarray can be rearranged into an arithmetic sequence or not.
            status = check_arithmetic(temp_array)

            # Append the result to the final_list
            final_list.append(status)

        # Return the final_list containing results for all subarray
        return final_list