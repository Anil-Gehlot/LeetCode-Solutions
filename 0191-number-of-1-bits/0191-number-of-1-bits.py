class Solution:
    def hammingWeight(self, n: int) -> int:
        
        # Convert the integer to its binary representation
        binary_representation = bin(n)

        # Initialize a counter for the number of '1' bits
        count_of_one_bits = 0

        # Iterate through each character in the binary representation
        for bit in binary_representation:
            
            # Check if the current bit is '1', and increment the counter
            if bit == "1":
                count_of_one_bits += 1

        # Return the final count of '1' bits
        return count_of_one_bits
