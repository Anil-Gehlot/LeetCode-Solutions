class Solution:
    def maxScore(self, s: str) -> int:
        
        # Initialize the total score variable
        total_score = 0

        # Check if the length of the string is less than or equal to 2
        if len(s) <= 2:
            
            # If the first character is '0', increment the total score
            if s[0] == '0':
                total_score += 1
                
            # If the second character is '1', increment the total score
            if s[1] == '1':
                total_score += 1
        else:
            
            # Iterate through the string up to the second-to-last character
            for i in range(len(s) - 1):
                
                zero_count = 0  # Initialize the count of '0's
                ones_count = 0  # Initialize the count of '1's

                # Count the number of '0's in the substring from the beginning up to index i
                for j in range(0, i + 1):
                    
                    if s[j] == "0":
                        zero_count += 1

                # Count the number of '1's in the substring from index i+1 to the end
                for k in range(i + 1, len(s)):
                    if s[k] == '1':
                        ones_count += 1

                # Calculate the temporary score for the current split
                temp_score = zero_count + ones_count

                # Update the total score with the maximum of the current and previous scores
                total_score = max(total_score, temp_score)

        # Return the final total score
        return total_score
