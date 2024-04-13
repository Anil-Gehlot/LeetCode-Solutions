class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        # Create a dictionary to store the indices of elements in nums
        nums_dict = dict()

        # Populate nums_dict with indices of elements in nums
        for i in range(len(nums)):
            nums_dict[nums[i]] = i
        
        # Iterate through each operation
        for operation in operations:
            # Get the index of the element to be replaced from nums_dict
            temp_val = nums_dict.get(operation[0])

            # Delete the element from nums_dict
            del nums_dict[operation[0]]

            # Update nums_dict with the new element
            nums_dict.update({operation[1]: temp_val})
        
        # Update nums with the new elements based on the modified nums_dict
        for key, value in nums_dict.items():
            nums[value] = key
        
        # Return the modified nums list
        return nums



        # # Time Limit Exceeded
        # for subarr in operations:
        #     ind = nums.index(subarr[0])
        #     nums[ind] = subarr[1]
        # return nums


        # # Time Limit Exceeded
        # for i in range(len(operations)):
        #     for j in range(len(nums)):
        #         if nums[j] == operations[i][0]:
        #             nums[j] = operations[i][1]
        # return nums


        # while operations:
        #     temp = operations.pop(0)

        #     for i in range(len(nums)):
        #         if nums[i] == temp[0]:
        #             nums[i] = temp[1]
        # return nums