class Solution:
    def winnerOfGame(self, colors: str) -> bool:


        count = 0

        for i in range(1, len(colors)-1):

            # counting how many times Alice wins
            if colors[i]=='A' and colors[i-1]=='A' and colors[i+1]=='A':
                count += 1

            # reducing counting if Bob wins
            elif colors[i]=='B' and colors[i-1]=='B' and colors[i+1]=='B':
                count -= 1
        
        # retruning True if Alice has greater count than zero
        if count > 0:
            return True
        # if alice has no greater count than zero then return False
        else:
            return False

        

