class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        # an empty list to store the scores
        new_score = []

        # Iterate through each record in the operations list
        for record in operations:
            
            # If the record is "D", double the last valid score and append it to the new_score list
            if record == "D":
                new_score.append(new_score[-1] * 2)
                
            # If the record is "C", remove the last valid score from the new_score list
            elif record == "C":
                new_score.pop()

            # If the record is "+", add the sum of the last two valid scores and append it to the new_score list
            elif record == "+":
                new_score.append(new_score[-1] + new_score[-2])
                
            # If the record is a number, convert it to an integer and append it to the new_score list
            else:
                new_score.append(int(record))
        
        # Return the sum of all the scores in the new_score list
        return sum(new_score)
