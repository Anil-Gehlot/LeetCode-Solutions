class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:

        # Create an empty list to store the count of '1's in each row
        count_of_ones = []
        
        # Count the number of '1's in each row and store the counts in the list
        for row in bank:
            ones_count = 0
            for char in row:
                if char == "1":
                    ones_count += 1

            # Add the count of '1's to the list if it's not zero
            if ones_count != 0:
                count_of_ones.append(ones_count)
        
        # Initialize the total count of laser beams
        total_laser_beams = 0

        # Iterate through the list of ones counts to calculate the total count of laser beams
        for idx in range(len(count_of_ones) - 1):

            contribution = count_of_ones[idx] * count_of_ones[idx+1]

            # Add the contribution to the total count
            total_laser_beams += contribution
        
        # Return the total count of laser beams
        return total_laser_beams
