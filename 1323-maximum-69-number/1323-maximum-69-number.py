

class Solution:
    def maximum69Number(self, num: int) -> int:
        # Convert the number to a string for easy manipulation
        num = str(num)

        # Iterate through the digits of the number
        for digit in range(len(num)):
            # Check if the current digit is '6'
            if num[digit] == '6':
                # Replace the first '6' with '9'
                num = num[:digit] + '9' + num[digit+1:]
                # Break out of the loop after the replacement
                break

        # Convert the modified string back to an integer and return
        return int(num)