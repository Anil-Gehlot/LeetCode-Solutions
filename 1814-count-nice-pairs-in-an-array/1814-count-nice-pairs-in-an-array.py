class Solution:
    def countNicePairs(self, nums: List[int]) -> int:

        # function to reverse the digits of a number
        def reverse_digits(num):
            num_str = str(num)
            return int(num_str[::-1])

        # Modulo value for handling large numbers
        modulo = 10**9 + 7

        # Dictionary to store the count of differences
        difference_count = {}

        # Variable to store the count of nice pairs
        nice_pairs_count = 0

        # Iterate through the given array
        for i in range(len(nums)):
            # Calculate the difference between the number and its reverse
            difference = nums[i] - reverse_digits(nums[i])

            # Update the count of nice pairs with the value in the dictionary
            nice_pairs_count = (nice_pairs_count + difference_count.get(difference, 0)) % modulo

            # Update the dictionary with the current difference
            if difference in difference_count:
                difference_count[difference] += 1
            else:
                difference_count[difference] = 1

        # Return the final count of nice pairs
        return nice_pairs_count

        
        
        
        '''
        
        Time Limit Exeeds
        
        # modulo for large values
        modulo = 10**9 + 7
        
        # Function to reverse a non-negative integer
        def rev(num):
            num = str(num)
            return int(num[::-1])

        # Initialize the count of nice pairs
        count = 0

        # Iterate through all pairs of indices in the array
        for i in range(len(nums)-1):
            
            for j in range(i+1, len(nums)):
                
                # Check if the conditions are satisfied
                if nums[i] + rev(nums[j]) == nums[j] + rev(nums[i]):
                    
                    # Increment the count if conditions are met
                    count += 1

        # Return the final count of nice pairs
        return count%modulo
        
        '''