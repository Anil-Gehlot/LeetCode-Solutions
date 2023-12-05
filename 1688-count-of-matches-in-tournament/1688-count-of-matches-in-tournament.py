class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        total_matches_played = 0

        # Continue the loop until there is only one team left (the winner).
        while n != 1:
            
            # Calculate the number of matches played in the current round.
            matches_in_current_round = n // 2

            # Update the total number of matches played.
            total_matches_played += matches_in_current_round

            # Determine the number of teams advancing to the next round.
            n = n - matches_in_current_round

        # Return the total number of matches played in the tournament.
        return total_matches_played