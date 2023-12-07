class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        # Iterate through the characters of num from right to left
        for current_index in range(len(num) - 1, -1, -1):
            
            # Check if the current digit is odd
            current_digit = int(num[current_index])
            
            if current_digit % 2 != 0:
                
                # Return the substring from the beginning of num up to the current index
                return num[:current_index + 1]

        # If no odd digit is found, return an empty string
        else:
            return ""
