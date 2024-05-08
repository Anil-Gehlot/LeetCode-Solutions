class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        # Make a copy of the scores and sort it in descending order
        copy_score = score[:]
        copy_score.sort(reverse=True)

        # list to store the ranks
        answer = [-1] * len(score)

        # Iterate through each score
        for i in range(len(score)):

            # Check if the score matches the highest score
            if score[i] == copy_score[0]:
                answer[i] = "Gold Medal"
                
            # Check if the score matches the second highest score
            elif score[i] == copy_score[1]:
                answer[i] = "Silver Medal"
                
            # Check if the score matches the third highest score
            elif score[i] == copy_score[2]:
                answer[i] = "Bronze Medal"
                
            else:
                # If not in top 3, assign the rank based on its index in sorted list
                answer[i] = f"{ copy_score.index(score[i]) + 1 }"
                
        return answer
