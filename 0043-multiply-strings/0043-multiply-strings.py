class Solution:
    def str_to_num(self, num: str) -> int:

        # handling trailing zeros separately.
        # Count trailing zeros and remove them from the end of the string
        zero_count = 0
        while num[-1] == "0":  
            zero_count += 1  
            num = num[:len(num) - 1]  
            
        final_num = 0  # Variable to hold the final converted number
        count = 10  # Multiplier to determine the place value of each digit

        # Loop through the string, processing each character from right to left
        while num:
            n = len(num)  # Length of the current string
            temp_num = ord(num[n - 1]) - ord("0")  # Convert the last character to its numeric value

            # If final_num is zero and the current numeric value is non-zero, set final_num
            if final_num == 0 and temp_num != 0:
                final_num = temp_num

            else:
                # Otherwise, add the current numeric value to final_num with the correct place value
                final_num = (temp_num * count) + final_num
                count *= 10  # Increase the multiplier by a factor of 10 for the next digit

            # Remove the last character from the string for the next iteration
            num = num[:n - 1]

        # Return the final number, accounting for the trailing zeros by multiplying by 10^zero_count
        return final_num * (10 ** zero_count)

    def num_to_str(self, num: int) -> str:

        num_str = ""  # Initialize the string to store the number

        while num:
            last_digit = num % 10  # Get the last digit
            num = num // 10  # Reduce the number by removing the last digit

            # Convert the last digit to its corresponding character
            last_digit = chr(last_digit + ord("0"))

            # Prepend the character to the result string to maintain the correct order
            num_str = last_digit + num_str

        return num_str  


    def multiply(self, num1: str, num2: str) -> str:

        # If either number is "0", the product is "0"
        if num1 == "0" or num2 == "0":
            return "0"

        # Convert the input strings to integers
        num1 = self.str_to_num(num1)
        num2 = self.str_to_num(num2)

        # Calculate the product of the two numbers
        multiply = num1 * num2

        # Convert the product back to a string and return it
        return self.num_to_str(multiply)
