
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        # Count the occurrences of each winner and loser using Counter
        winner_counter = Counter([matches[x][0] for x in range(len(matches))])
        losser_counter = Counter([matches[x][1] for x in range(len(matches))])


        # Initialize the result as two empty lists
        result = [[], sorted([])]

        # Iterate through the winners
        for key in winner_counter:
            
            # If the winner is not a loser, add them to the list of players with no losses
            if key not in losser_counter:
                result[0].append(key)

        # Iterate through the losers
        for key in losser_counter:
            
            # If the loser lost only one match, add them to the list of players with one loss
            if losser_counter[key] == 1:
                result[1].append(key)

        # Sort both lists
        for i in result:
            i.sort()

        # Return the final result
        return result