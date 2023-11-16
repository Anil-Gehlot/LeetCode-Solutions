class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        
        # Convert banned list to a set for faster lookup
        banned = set(banned)

        # Initialize variables to keep track of sums and count
        previous_sum = 0
        current_sum = 0
        count = 0

        # Iterate through the range [1, n]
        for num in range(1, n + 1):
            
            # Check if the current number is not in the banned set
            if num not in banned:
                
                # Update the current sum with the current number
                current_sum += num

                # Check if the current sum exceeds the maximum sum
                if current_sum > maxSum:
                    
                    # If it does, return the current count
                    return count
                
                else:
                    
                    # If not, update the previous sum and increment the count
                    previous_sum = current_sum
                    count += 1

        # Return the final count after iterating through the range
        return count
