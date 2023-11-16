class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        # Convert the input list to a set for faster lookups
        nums_set = set(nums)
        
        # List to store missing numbers
        missing_nums = []
        
        # Iterate through numbers from 1 to the length of nums
        for number in range(1, len(nums)+1):
            
            # Check if the number is not in the set
            if number not in nums_set:
                
                # Append the missing number to the result list
                missing_nums.append(number)
                
        # Return the list of missing numbers
        return missing_nums
