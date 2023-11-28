class Solution:
    def numberOfWays(self, corridor: str) -> int:
        
        # a variable for modulo operation
        MOD = 10**9 + 7

        # a variable to count the number of seats in the corridor
        seats_count = 0

        # Counting the number of seats in the corridor
        for seat in corridor:
            if seat == "S":
                seats_count += 1

        # If there are no seats or an odd number of seats, return 0
        if seats_count == 0 or seats_count % 2 != 0:
            return 0

        # a list to store the indexes of seats in the corridor
        seats_indexes = []

        # finding the indexes of seats in the corridor
        for index in range(len(corridor)):
            if corridor[index] == "S":
                seats_indexes.append(index)

        # a variable to store the final result, starting with 1
        total_ways = 1

        # iterating seat_indexes to calculate the number of ways to place dividers
        for divider in range(2, len(seats_indexes), 2):
            
            # Calculate the total number of positions for dividers in the current section
            total_divider = seats_indexes[divider] - seats_indexes[divider - 1]
            
            # Multiply the total ways by the number of positions for dividers in the current section
            total_ways = (total_ways * total_divider) % MOD

        # Return the final result after all calculations
        return total_ways
