class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        # Variable to store the integer representation of `num`
        integer_num = 0  

        # Convert `num` from array form to an integer
        for number in num:
            if number == 0:
                # If the current digit is zero, multiply the current integer by 10 to maintain position
                integer_num *= 10
            else:
                # If the current digit is non-zero, append it to `integer_num`
                integer_num = (integer_num * 10) + number
        
        # Add `k` to the converted integer
        addition = integer_num + k  # Sum of `integer_num` and `k`

        result = []  # List to store the result in array form

        # Convert `addition` back to array form by extracting each digit
        while addition:
            last_digit = addition % 10  # Get the last digit
            addition = addition // 10  # Remove the last digit

            # Insert the extracted digit at the beginning of the result list
            result.insert(0, last_digit)
        
        return result  # Return the array-form representation of the sum

            